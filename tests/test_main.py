import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport

# Add the project root to the path to allow importing 'scripts'
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.main import app

@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)

@pytest.mark.asyncio
async def test_chat_with_pm_agent_mocked():
    """
    Tests the /api/v1/chat/{agent_name} endpoint with a mocked LLM call.
    """
    # The dictionary that the mocked function will return
    mock_response_payload = {
        "agent": "PM",
        "response": "This is a mocked response from the PM agent."
    }

    # Use patch to replace 'call_ollama_agent' in the 'scripts.main' module
    with patch('scripts.main.call_ollama_agent', return_value=mock_response_payload) as mock_ollama_call:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            # The data to send in the POST request
            chat_data = {"message": "Create a new character."}
            response = await ac.post("/api/v1/chat/PM", json=chat_data)

        # Assertions
        assert response.status_code == 200
        assert response.json() == mock_response_payload
        
        # Verify that the mocked function was called exactly once with the correct arguments
        mock_ollama_call.assert_called_once_with("PM", "Create a new character.")

@pytest.mark.asyncio
async def test_integrate_and_playtest_endpoint():
    """
    Tests the placeholder /api/v1/integrate_and_playtest endpoint.
    """
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/v1/integrate_and_playtest")

    assert response.status_code == 200
    expected_json = {"status": "success", "message": "Integration process initiated."}
    assert response.json() == expected_json