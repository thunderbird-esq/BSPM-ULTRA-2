document.addEventListener('DOMContentLoaded', () => {
    // --- STATE MANAGEMENT ---
    const App = {
        selectedAgent: 'PM',
        chatHistory: {
            'PM': [], 'Art': [], 'Writing': [], 'Code': [], 'QA': [], 'Sound': []
        },
        agentNames: {
            'PM': 'Project Manager', 'Art': 'Art Director', 'Writing': 'Writing Director',
            'Code': 'Code Director', 'QA': 'QA Director', 'Sound': 'Sound Director',
            'System': 'System', 'User': 'Director (You)'
        }
    };

    // --- DOM ELEMENTS ---
    const departmentLinks = document.querySelectorAll('.department-link');
    const chatLog = document.getElementById('chat-log');
    const chatForm = document.getElementById('chat-form');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');
    const playtestButton = document.getElementById('playtest-button');
    const currentAgentNameEl = document.getElementById('current-agent-name');
    const connectionStatusEl = document.getElementById('connection-status');
    const websocketStatusEl = document.getElementById('websocket-status');
    const activeTasksList = document.getElementById('active-tasks-list');

    // --- AGENT & CHAT LOGIC ---
    function selectAgent(agentId) {
        if (!agentId || !App.agentNames[agentId]) return;
        
        App.selectedAgent = agentId;

        departmentLinks.forEach(link => {
            link.classList.toggle('active', link.dataset.agent === agentId);
        });

        currentAgentNameEl.textContent = App.agentNames[agentId];
        messageInput.placeholder = `Enter command for ${App.agentNames[agentId]}...`;
        renderChatHistory();
    }

    function addMessage(agentId, sender, content, isHtml = false) {
        const message = {
            sender: sender, // 'user', 'agent', 'system', 'error'
            content: content,
            isHtml: isHtml,
            timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        };
        
        if (!App.chatHistory[agentId]) {
            App.chatHistory[agentId] = [];
        }
        App.chatHistory[agentId].push(message);

        if (agentId === App.selectedAgent) {
            renderChatHistory();
        }
    }

    function renderChatHistory() {
        chatLog.innerHTML = '';
        const history = App.chatHistory[App.selectedAgent] || [];

        history.forEach(msg => {
            const messageEl = document.createElement('article');
            messageEl.className = `chat-message ${msg.sender}`;
            
            const senderName = msg.sender === 'agent' ? App.agentNames[App.selectedAgent] : App.agentNames[msg.sender] || 'Unknown';
            const iconClass = `${msg.sender}-icon`;
            const iconChar = senderName.charAt(0);

            messageEl.innerHTML = `
                <header><span class="${iconClass}">${iconChar}</span>${senderName}</header>
                <div class="content">${msg.isHtml ? msg.content : `<p>${msg.content.replace(/\n/g, '<br>')}</p>`}</div>
                <footer><time>${msg.timestamp}</time></footer>
            `;
            chatLog.appendChild(messageEl);
        });
        chatLog.scrollTop = chatLog.scrollHeight;
    }

    async function handleUserInput() {
        const messageText = messageInput.value.trim();
        if (!messageText) return;

        const agent = App.selectedAgent;
        addMessage(agent, 'user', messageText);
        messageInput.value = '';
        sendButton.disabled = true;
        
        const typingIndicator = showTypingIndicator();

        try {
            const response = await fetch(`/api/v1/chat/${agent}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: messageText, history: App.chatHistory[agent] })
            });

            if (!response.ok) {
                const err = await response.json();
                throw new Error(err.detail || `Server Error: ${response.statusText}`);
            }

            const result = await response.json();
            
            let responseContent = `<pre>${JSON.stringify(result, null, 2)}</pre>`;
            if(result.response) {
                responseContent = result.response;
            }
            
            addMessage(agent, 'agent', responseContent, true);

        } catch (error) {
            addMessage(agent, 'error', `<b>Error:</b> ${error.message}`, true);
        } finally {
            typingIndicator.remove();
            sendButton.disabled = false;
            messageInput.focus();
        }
    }
    
    function showTypingIndicator() {
        const typingEl = document.createElement('div');
        typingEl.className = 'typing-indicator';
        typingEl.innerHTML = `
            <span>${App.agentNames[App.selectedAgent]} is typing</span>
            <div class="typing-dots"><div></div><div></div><div></div></div>
        `;
        chatLog.appendChild(typingEl);
        chatLog.scrollTop = chatLog.scrollHeight;
        return typingEl;
    }

    // --- WEBSOCKET LOGIC ---
    function setupWebSocket() {
        const ws = new WebSocket(`ws://${window.location.host}/ws`);

        ws.onopen = () => {
            connectionStatusEl.textContent = "ONLINE";
            connectionStatusEl.style.color = "var(--color-accent)";
            websocketStatusEl.textContent = "Real-time link established.";
            addMessage('PM', 'system', 'Connection to Command Deck established. Systems online.');
        };

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            updateActiveTask(data);
        };

        ws.onclose = () => {
            connectionStatusEl.textContent = "OFFLINE";
            connectionStatusEl.style.color = "var(--color-error)";
            websocketStatusEl.textContent = "Connection lost. Retrying...";
            setTimeout(setupWebSocket, 5000);
        };
        
        ws.onerror = () => {
            websocketStatusEl.textContent = "Connection error.";
            ws.close();
        }
    }

    function updateActiveTask(data) {
        let taskEl = document.getElementById(`task-${data.asset_id}`);
        if (!taskEl) {
            taskEl = document.createElement('div');
            taskEl.id = `task-${data.asset_id}`;
            taskEl.className = 'task-item';
            activeTasksList.prepend(taskEl);
        }

        let approveButton = '';
        let assetImage = '';

        if (data.status === 'COMPLETED' && data.image_url) {
            assetImage = `<img src="${data.image_url}?t=${new Date().getTime()}" class="asset-image" alt="Generated Asset">`;
            approveButton = `<button class="approve-button" onclick="window.approveAsset(${data.asset_id}, '${data.asset_type || 'sprite'}')">Approve</button>`;
        }

        taskEl.innerHTML = `
            <header>${data.name || 'Untitled Task'}</header>
            <div class="status ${data.status}">${data.status}</div>
            ${assetImage}
            ${data.message ? `<p class="error-details">${data.message}</p>` : ''}
            ${approveButton}
        `;
    }

    // --- ASSET & PLAYTEST LOGIC ---
    window.approveAsset = async (assetId, assetType) => {
        const taskEl = document.getElementById(`task-${assetId}`);
        const button = taskEl.querySelector('.approve-button');
        button.textContent = "Approving...";
        button.disabled = true;

        try {
            const response = await fetch('/api/v1/approve_asset', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ asset_id: assetId, asset_type: assetType })
            });
            if (!response.ok) {
                const err = await response.json();
                throw new Error(err.detail || 'Approval failed on the backend.');
            }
            const result = await response.json();
            taskEl.querySelector('.status').textContent = 'APPROVED';
            button.textContent = 'Approved!';
            taskEl.style.borderColor = 'var(--color-accent)';
            addMessage('PM', 'system', `Asset "${result.task_name}" (ID: ${assetId}) has been approved and moved to the project folder.`);

        } catch (error) {
            button.textContent = "Error";
            button.style.borderColor = "var(--color-error)";
            addMessage('PM', 'error', `<b>Error:</b> ${error.message}`, true);
        }
    };

    async function handlePlaytest() {
        playtestButton.textContent = "Integrating...";
        playtestButton.disabled = true;
        addMessage('PM', 'system', 'Initiating integration and playtest sequence...');

        try {
            const response = await fetch('/api/v1/integrate_and_playtest', { method: 'POST' });
            const result = await response.json();
            if (!response.ok) {
                throw new Error(result.message || 'Integration failed');
            }
            addMessage('PM', 'system', `Integration successful! Moved ${result.moved_assets.length} assets. Emulator launched.`, true);
            playtestButton.textContent = "Launch Success!";
            playtestButton.style.backgroundColor = "var(--color-accent)";
            playtestButton.style.color = "var(--color-bg)";

        } catch (error) {
            addMessage('PM', 'error', `<b>Integration Error:</b> ${error.message}`, true);
            playtestButton.textContent = "Launch Failed";
            playtestButton.style.backgroundColor = "var(--color-error)";
            playtestButton.style.color = "#fff";
        } finally {
            setTimeout(() => {
                playtestButton.textContent = "Integrate & Playtest";
                playtestButton.disabled = false;
                playtestButton.style.backgroundColor = "";
                playtestButton.style.color = "";
            }, 3000);
        }
    }

    // --- INITIALIZATION ---
    function init() {
        departmentLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                selectAgent(link.dataset.agent);
            });
        });

        chatForm.addEventListener('submit', (e) => {
            e.preventDefault();
            handleUserInput();
        });
        
        playtestButton.addEventListener('click', handlePlaytest);

        selectAgent('PM');
        setupWebSocket();
    }

    init();
});