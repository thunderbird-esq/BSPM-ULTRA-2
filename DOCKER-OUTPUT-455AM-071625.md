2025-07-16 04:09:13 gbstudio_hub-ollama-1   | time=2025-07-16T08:09:13.836Z level=INFO source=routes.go:1235 msg="server config" env="map[CUDA_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VERSION: HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_CONTEXT_LENGTH:4096 OLLAMA_DEBUG:INFO OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://0.0.0.0:11434 OLLAMA_INTEL_GPU:false OLLAMA_KEEP_ALIVE:5m0s OLLAMA_KV_CACHE_TYPE: OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:/root/.ollama/models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NEW_ENGINE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:0 OLLAMA_ORIGINS:[http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://* vscode-webview://* vscode-file://*] OLLAMA_SCHED_SPREAD:false ROCR_VISIBLE_DEVICES: http_proxy: https_proxy: no_proxy:]"
2025-07-16 04:09:13 gbstudio_hub-ollama-1   | time=2025-07-16T08:09:13.993Z level=INFO source=images.go:476 msg="total blobs: 56"
2025-07-16 04:09:14 gbstudio_hub-ollama-1   | time=2025-07-16T08:09:14.033Z level=INFO source=images.go:483 msg="total unused blobs removed: 0"
2025-07-16 04:09:14 gbstudio_hub-ollama-1   | time=2025-07-16T08:09:14.040Z level=INFO source=routes.go:1288 msg="Listening on [::]:11434 (version 0.9.6)"
2025-07-16 04:09:14 gbstudio_hub-ollama-1   | time=2025-07-16T08:09:14.041Z level=INFO source=gpu.go:217 msg="looking for compatible GPUs"
2025-07-16 04:09:14 gbstudio_hub-ollama-1   | time=2025-07-16T08:09:14.044Z level=INFO source=gpu.go:377 msg="no compatible GPUs were discovered"
2025-07-16 04:09:14 gbstudio_hub-ollama-1   | time=2025-07-16T08:09:14.044Z level=INFO source=types.go:130 msg="inference compute" id=0 library=cpu variant="" compute="" driver=0.0 name="" total="7.7 GiB" available="7.0 GiB"
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | time=2025-07-16T08:18:25.214Z level=INFO source=server.go:135 msg="system memory" total="7.7 GiB" free="6.5 GiB" free_swap="731.4 MiB"
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | time=2025-07-16T08:18:25.219Z level=INFO source=server.go:175 msg=offload library=cpu layers.requested=-1 layers.model=33 layers.offload=0 layers.split="" memory.available="[6.5 GiB]" memory.gpu_overhead="0 B" memory.required.full="5.8 GiB" memory.required.partial="0 B" memory.required.kv="1.0 GiB" memory.required.allocations="[5.8 GiB]" memory.weights.total="4.1 GiB" memory.weights.repeating="3.7 GiB" memory.weights.nonrepeating="411.0 MiB" memory.graph.full="560.0 MiB" memory.graph.partial="677.5 MiB"
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: loaded meta data with 22 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-6a0746a1ec1aef3e7ec53868f220ff6e389f6f8ef87a01d77c96807de94ca2aa (version GGUF V3 (latest))
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv   0:                       general.architecture str              = llama
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv   1:                               general.name str              = Meta-Llama-3-8B-Instruct
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv   2:                          llama.block_count u32              = 32
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv   3:                       llama.context_length u32              = 8192
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv   6:                 llama.attention.head_count u32              = 32
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv   7:              llama.attention.head_count_kv u32              = 8
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv   8:                       llama.rope.freq_base f32              = 500000.000000
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv  10:                          general.file_type u32              = 2
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv  11:                           llama.vocab_size u32              = 128256
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv  12:                 llama.rope.dimension_count u32              = 128
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv  13:                       tokenizer.ggml.model str              = gpt2
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv  14:                         tokenizer.ggml.pre str              = llama-bpe
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv  15:                      tokenizer.ggml.tokens arr[str,128256]  = ["!", "\"", "#", "$", "%", "&", "'", ...
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv  16:                  tokenizer.ggml.token_type arr[i32,128256]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv  17:                      tokenizer.ggml.merges arr[str,280147]  = ["Ġ Ġ", "Ġ ĠĠĠ", "ĠĠ ĠĠ", "...
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv  18:                tokenizer.ggml.bos_token_id u32              = 128000
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv  19:                tokenizer.ggml.eos_token_id u32              = 128009
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv  20:                    tokenizer.chat_template str              = {% set loop_messages = messages %}{% ...
2025-07-16 04:09:15 gbstudio_hub-backend-1  | INFO:     Started server process [1]
2025-07-16 04:09:15 gbstudio_hub-backend-1  | INFO:     Waiting for application startup.
2025-07-16 04:09:15 gbstudio_hub-backend-1  | 2025-07-16 08:09:15,262 - INFO - Database initialized successfully.
2025-07-16 04:09:15 gbstudio_hub-backend-1  | 2025-07-16 08:09:15,262 - INFO - Pixel art workflow is available at /ComfyUI/workflows/workflow_pixel_art.json
2025-07-16 04:09:15 gbstudio_hub-backend-1  | INFO:     Application startup complete.
2025-07-16 04:09:15 gbstudio_hub-backend-1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
2025-07-16 04:09:20 gbstudio_hub-backend-1  | INFO:     192.168.176.1:55270 - "GET / HTTP/1.1" 200 OK
2025-07-16 04:09:42 gbstudio_hub-backend-1  | INFO:     192.168.176.1:55272 - "GET / HTTP/1.1" 200 OK
2025-07-16 04:09:42 gbstudio_hub-backend-1  | INFO:     192.168.176.1:55272 - "GET /static/css/main.css HTTP/1.1" 200 OK
2025-07-16 04:09:42 gbstudio_hub-backend-1  | INFO:     192.168.176.1:55286 - "GET /static/js/app.js HTTP/1.1" 200 OK
2025-07-16 04:09:42 gbstudio_hub-backend-1  | INFO:     192.168.176.1:55290 - "WebSocket /ws" [accepted]
2025-07-16 04:09:42 gbstudio_hub-backend-1  | INFO:     connection open
2025-07-16 04:09:42 gbstudio_hub-backend-1  | INFO:     192.168.176.1:55272 - "GET /favicon.ico HTTP/1.1" 404 Not Found
2025-07-16 04:22:38 gbstudio_hub-backend-1  | INFO:     192.168.176.1:61792 - "POST /api/v1/chat/PM HTTP/1.1" 200 OK
2025-07-16 04:22:38 gbstudio_hub-backend-1  | ERROR:    Exception in ASGI application
2025-07-16 04:22:38 gbstudio_hub-backend-1  | Traceback (most recent call last):
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     result = await app(  # type: ignore[func-returns-value]
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     return await self.app(scope, receive, send)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/fastapi/applications.py", line 1054, in __call__
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await super().__call__(scope, receive, send)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/applications.py", line 113, in __call__
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await self.middleware_stack(scope, receive, send)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     raise exc
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await self.app(scope, receive, _send)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await self.app(scope, receive, send)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     raise exc
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await app(scope, receive, sender)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 716, in __call__
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await self.middleware_stack(scope, receive, send)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 736, in app
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await route.handle(scope, receive, send)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 290, in handle
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await self.app(scope, receive, send)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 78, in app
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - kv  21:               general.quantization_version u32              = 2
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - type  f32:   65 tensors
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - type q4_0:  225 tensors
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | llama_model_loader: - type q6_K:    1 tensors
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | print_info: file format = GGUF V3 (latest)
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | print_info: file type   = Q4_0
2025-07-16 04:18:25 gbstudio_hub-ollama-1   | print_info: file size   = 4.33 GiB (4.64 BPW) 
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | load: special tokens cache size = 256
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | load: token to piece cache size = 0.8000 MB
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: arch             = llama
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     raise exc
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await app(scope, receive, sender)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 76, in app
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await response(scope, receive, send)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/responses.py", line 168, in __call__
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await self.background()
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/background.py", line 42, in __call__
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await task()
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/background.py", line 29, in __call__
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     await run_in_threadpool(self.func, *self.args, **self.kwargs)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/concurrency.py", line 38, in run_in_threadpool
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: vocab_only       = 1
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: model type       = ?B
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: model params     = 8.03 B
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: general.name     = Meta-Llama-3-8B-Instruct
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: vocab type       = BPE
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: n_vocab          = 128256
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: n_merges         = 280147
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: BOS token        = 128000 '<|begin_of_text|>'
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: EOS token        = 128009 '<|eot_id|>'
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: EOT token        = 128009 '<|eot_id|>'
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: LF token         = 198 'Ċ'
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: EOG token        = 128009 '<|eot_id|>'
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: max token length = 256
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_load: vocab only - skipping tensors
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     return await anyio.to_thread.run_sync(func)
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/anyio/to_thread.py", line 56, in run_sync
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     return await get_async_backend().run_sync_in_worker_thread(
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/anyio/_backends/_asyncio.py", line 2470, in run_sync_in_worker_thread
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     return await future
2025-07-16 04:22:38 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/anyio/_backends/_asyncio.py", line 967, in run
2025-07-16 04:22:38 gbstudio_hub-backend-1  |     result = context.run(func, *args)
2025-07-16 04:22:38 gbstudio_hub-backend-1  | TypeError: log_chat_message() got an unexpected keyword argument 'agent_name'
2025-07-16 04:25:22 gbstudio_hub-backend-1  | INFO:     192.168.176.1:58316 - "GET /static/css/main.css HTTP/1.1" 304 Not Modified
2025-07-16 04:27:44 gbstudio_hub-backend-1  | INFO:     192.168.176.1:57496 - "POST /api/v1/chat/Art HTTP/1.1" 200 OK
2025-07-16 04:27:44 gbstudio_hub-backend-1  | ERROR:    Exception in ASGI application
2025-07-16 04:27:44 gbstudio_hub-backend-1  | Traceback (most recent call last):
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | time=2025-07-16T08:18:26.380Z level=INFO source=server.go:438 msg="starting llama server" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-6a0746a1ec1aef3e7ec53868f220ff6e389f6f8ef87a01d77c96807de94ca2aa --ctx-size 8192 --batch-size 512 --threads 4 --no-mmap --parallel 2 --port 42357"
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     result = await app(  # type: ignore[func-returns-value]
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     return await self.app(scope, receive, send)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/fastapi/applications.py", line 1054, in __call__
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await super().__call__(scope, receive, send)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/applications.py", line 113, in __call__
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await self.middleware_stack(scope, receive, send)
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | time=2025-07-16T08:18:26.381Z level=INFO source=sched.go:483 msg="loaded runners" count=1
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | time=2025-07-16T08:18:26.381Z level=INFO source=server.go:598 msg="waiting for llama runner to start responding"
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | time=2025-07-16T08:18:26.383Z level=INFO source=server.go:632 msg="waiting for server to become available" status="llm server not responding"
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | time=2025-07-16T08:18:26.461Z level=INFO source=runner.go:815 msg="starting go runner"
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-haswell.so
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | time=2025-07-16T08:18:26.517Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | time=2025-07-16T08:18:26.530Z level=INFO source=runner.go:874 msg="Server listening on 127.0.0.1:42357"
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | time=2025-07-16T08:18:26.639Z level=INFO source=server.go:632 msg="waiting for server to become available" status="llm server loading model"
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     raise exc
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await self.app(scope, receive, _send)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await self.app(scope, receive, send)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     raise exc
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await app(scope, receive, sender)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 716, in __call__
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await self.middleware_stack(scope, receive, send)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 736, in app
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await route.handle(scope, receive, send)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 290, in handle
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await self.app(scope, receive, send)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 78, in app
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     raise exc
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await app(scope, receive, sender)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 76, in app
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await response(scope, receive, send)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/responses.py", line 168, in __call__
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await self.background()
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/background.py", line 42, in __call__
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await task()
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/background.py", line 29, in __call__
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: loaded meta data with 22 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-6a0746a1ec1aef3e7ec53868f220ff6e389f6f8ef87a01d77c96807de94ca2aa (version GGUF V3 (latest))
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv   0:                       general.architecture str              = llama
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv   1:                               general.name str              = Meta-Llama-3-8B-Instruct
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv   2:                          llama.block_count u32              = 32
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv   3:                       llama.context_length u32              = 8192
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv   6:                 llama.attention.head_count u32              = 32
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     await run_in_threadpool(self.func, *self.args, **self.kwargs)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/concurrency.py", line 38, in run_in_threadpool
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     return await anyio.to_thread.run_sync(func)
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/anyio/to_thread.py", line 56, in run_sync
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     return await get_async_backend().run_sync_in_worker_thread(
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/anyio/_backends/_asyncio.py", line 2470, in run_sync_in_worker_thread
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     return await future
2025-07-16 04:27:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/anyio/_backends/_asyncio.py", line 967, in run
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv   7:              llama.attention.head_count_kv u32              = 8
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv   8:                       llama.rope.freq_base f32              = 500000.000000
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
2025-07-16 04:27:44 gbstudio_hub-backend-1  |     result = context.run(func, *args)
2025-07-16 04:27:44 gbstudio_hub-backend-1  | TypeError: log_chat_message() got an unexpected keyword argument 'agent_name'
2025-07-16 04:33:44 gbstudio_hub-backend-1  | INFO:     192.168.176.1:61628 - "POST /api/v1/chat/Art HTTP/1.1" 200 OK
2025-07-16 04:33:44 gbstudio_hub-backend-1  | ERROR:    Exception in ASGI application
2025-07-16 04:33:44 gbstudio_hub-backend-1  | Traceback (most recent call last):
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     result = await app(  # type: ignore[func-returns-value]
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     return await self.app(scope, receive, send)
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/fastapi/applications.py", line 1054, in __call__
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv  10:                          general.file_type u32              = 2
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await super().__call__(scope, receive, send)
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv  11:                           llama.vocab_size u32              = 128256
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv  12:                 llama.rope.dimension_count u32              = 128
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv  13:                       tokenizer.ggml.model str              = gpt2
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv  14:                         tokenizer.ggml.pre str              = llama-bpe
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/applications.py", line 113, in __call__
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await self.middleware_stack(scope, receive, send)
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv  15:                      tokenizer.ggml.tokens arr[str,128256]  = ["!", "\"", "#", "$", "%", "&", "'", ...
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv  16:                  tokenizer.ggml.token_type arr[i32,128256]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv  17:                      tokenizer.ggml.merges arr[str,280147]  = ["Ġ Ġ", "Ġ ĠĠĠ", "ĠĠ ĠĠ", "...
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv  18:                tokenizer.ggml.bos_token_id u32              = 128000
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv  19:                tokenizer.ggml.eos_token_id u32              = 128009
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv  20:                    tokenizer.chat_template str              = {% set loop_messages = messages %}{% ...
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - kv  21:               general.quantization_version u32              = 2
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - type  f32:   65 tensors
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - type q4_0:  225 tensors
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | llama_model_loader: - type q6_K:    1 tensors
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: file format = GGUF V3 (latest)
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: file type   = Q4_0
2025-07-16 04:18:26 gbstudio_hub-ollama-1   | print_info: file size   = 4.33 GiB (4.64 BPW) 
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | load: special tokens cache size = 256
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     raise exc
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await self.app(scope, receive, _send)
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | load: token to piece cache size = 0.8000 MB
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: arch             = llama
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: vocab_only       = 0
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_ctx_train      = 8192
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_embd           = 4096
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_layer          = 32
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_head           = 32
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_head_kv        = 8
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_rot            = 128
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_swa            = 0
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await self.app(scope, receive, send)
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     raise exc
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_swa_pattern    = 1
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await app(scope, receive, sender)
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 716, in __call__
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await self.middleware_stack(scope, receive, send)
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 736, in app
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await route.handle(scope, receive, send)
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 290, in handle
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await self.app(scope, receive, send)
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 78, in app
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     raise exc
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await app(scope, receive, sender)
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 76, in app
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await response(scope, receive, send)
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/responses.py", line 168, in __call__
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await self.background()
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/background.py", line 42, in __call__
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await task()
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/background.py", line 29, in __call__
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     await run_in_threadpool(self.func, *self.args, **self.kwargs)
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/starlette/concurrency.py", line 38, in run_in_threadpool
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     return await anyio.to_thread.run_sync(func)
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/anyio/to_thread.py", line 56, in run_sync
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     return await get_async_backend().run_sync_in_worker_thread(
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/anyio/_backends/_asyncio.py", line 2470, in run_sync_in_worker_thread
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     return await future
2025-07-16 04:33:44 gbstudio_hub-backend-1  |   File "/usr/local/lib/python3.9/site-packages/anyio/_backends/_asyncio.py", line 967, in run
2025-07-16 04:33:44 gbstudio_hub-backend-1  |     result = context.run(func, *args)
2025-07-16 04:33:44 gbstudio_hub-backend-1  | TypeError: log_chat_message() got an unexpected keyword argument 'agent_name'
2025-07-16 04:38:32 gbstudio_hub-backend-1  | INFO:     Shutting down
2025-07-16 04:38:32 gbstudio_hub-backend-1  | INFO:     connection closed
2025-07-16 04:38:32 gbstudio_hub-backend-1  | INFO:     Waiting for application shutdown.
2025-07-16 04:38:32 gbstudio_hub-backend-1  | INFO:     Application shutdown complete.
2025-07-16 04:38:32 gbstudio_hub-backend-1  | INFO:     Finished server process [1]
2025-07-16 04:38:34 gbstudio_hub-backend-1  | INFO:     Started server process [1]
2025-07-16 04:38:34 gbstudio_hub-backend-1  | INFO:     Waiting for application startup.
2025-07-16 04:38:34 gbstudio_hub-backend-1  | 2025-07-16 08:38:34,959 - INFO - Database initialized successfully.
2025-07-16 04:38:34 gbstudio_hub-backend-1  | 2025-07-16 08:38:34,959 - INFO - Pixel art workflow is available at /ComfyUI/workflows/workflow_pixel_art.json
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_embd_head_k    = 128
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_embd_head_v    = 128
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_gqa            = 4
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_embd_k_gqa     = 1024
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_embd_v_gqa     = 1024
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: f_norm_eps       = 0.0e+00
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: f_norm_rms_eps   = 1.0e-05
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: f_clamp_kqv      = 0.0e+00
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: f_max_alibi_bias = 0.0e+00
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: f_logit_scale    = 0.0e+00
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: f_attn_scale     = 0.0e+00
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_ff             = 14336
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_expert         = 0
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_expert_used    = 0
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: causal attn      = 1
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: pooling type     = 0
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: rope type        = 0
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: rope scaling     = linear
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: freq_base_train  = 500000.0
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: freq_scale_train = 1
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_ctx_orig_yarn  = 8192
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: rope_finetuned   = unknown
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: ssm_d_conv       = 0
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: ssm_d_inner      = 0
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: ssm_d_state      = 0
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: ssm_dt_rank      = 0
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: ssm_dt_b_c_rms   = 0
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: model type       = 8B
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: model params     = 8.03 B
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: general.name     = Meta-Llama-3-8B-Instruct
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: vocab type       = BPE
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_vocab          = 128256
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: n_merges         = 280147
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: BOS token        = 128000 '<|begin_of_text|>'
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: EOS token        = 128009 '<|eot_id|>'
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: EOT token        = 128009 '<|eot_id|>'
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: LF token         = 198 'Ċ'
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: EOG token        = 128009 '<|eot_id|>'
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | print_info: max token length = 256
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | load_tensors: loading model tensors, this can take a while... (mmap = false)
2025-07-16 04:18:27 gbstudio_hub-ollama-1   | load_tensors:          CPU model buffer size =  4437.80 MiB
2025-07-16 04:20:09 gbstudio_hub-ollama-1   | time=2025-07-16T08:20:09.879Z level=INFO source=server.go:632 msg="waiting for server to become available" status="llm server not responding"
2025-07-16 04:20:10 gbstudio_hub-ollama-1   | time=2025-07-16T08:20:10.142Z level=INFO source=server.go:632 msg="waiting for server to become available" status="llm server loading model"
2025-07-16 04:20:43 gbstudio_hub-ollama-1   | llama_context: constructing llama_context
2025-07-16 04:20:43 gbstudio_hub-ollama-1   | llama_context: n_seq_max     = 2
2025-07-16 04:20:43 gbstudio_hub-ollama-1   | llama_context: n_ctx         = 8192
2025-07-16 04:20:43 gbstudio_hub-ollama-1   | llama_context: n_ctx_per_seq = 4096
2025-07-16 04:20:43 gbstudio_hub-ollama-1   | llama_context: n_batch       = 1024
2025-07-16 04:20:43 gbstudio_hub-ollama-1   | llama_context: n_ubatch      = 512
2025-07-16 04:20:43 gbstudio_hub-ollama-1   | llama_context: causal_attn   = 1
2025-07-16 04:20:43 gbstudio_hub-ollama-1   | llama_context: flash_attn    = 0
2025-07-16 04:20:43 gbstudio_hub-ollama-1   | llama_context: freq_base     = 500000.0
2025-07-16 04:20:43 gbstudio_hub-ollama-1   | llama_context: freq_scale    = 1
2025-07-16 04:20:43 gbstudio_hub-ollama-1   | llama_context: n_ctx_per_seq (4096) < n_ctx_train (8192) -- the full capacity of the model will not be utilized
2025-07-16 04:20:43 gbstudio_hub-ollama-1   | llama_context:        CPU  output buffer size =     1.01 MiB
2025-07-16 04:20:43 gbstudio_hub-ollama-1   | llama_kv_cache_unified: kv_size = 8192, type_k = 'f16', type_v = 'f16', n_layer = 32, can_shift = 1, padding = 32
2025-07-16 04:20:47 gbstudio_hub-ollama-1   | llama_kv_cache_unified:        CPU KV buffer size =  1024.00 MiB
2025-07-16 04:20:47 gbstudio_hub-ollama-1   | llama_kv_cache_unified: KV self size  = 1024.00 MiB, K (f16):  512.00 MiB, V (f16):  512.00 MiB
2025-07-16 04:20:47 gbstudio_hub-ollama-1   | llama_context:        CPU compute buffer size =   560.01 MiB
2025-07-16 04:20:47 gbstudio_hub-ollama-1   | llama_context: graph nodes  = 1094
2025-07-16 04:20:47 gbstudio_hub-ollama-1   | llama_context: graph splits = 1
2025-07-16 04:20:47 gbstudio_hub-ollama-1   | time=2025-07-16T08:20:47.858Z level=INFO source=server.go:637 msg="llama runner started in 141.59 seconds"
2025-07-16 04:22:38 gbstudio_hub-ollama-1   | [GIN] 2025/07/16 - 08:22:38 | 200 |         4m14s |   192.168.176.4 | POST     "/api/generate"
2025-07-16 04:27:44 gbstudio_hub-ollama-1   | [GIN] 2025/07/16 - 08:27:44 | 200 |         4m20s |   192.168.176.4 | POST     "/api/generate"
2025-07-16 04:33:44 gbstudio_hub-ollama-1   | [GIN] 2025/07/16 - 08:33:44 | 200 |         1m13s |   192.168.176.4 | POST     "/api/generate"
2025-07-16 04:38:34 gbstudio_hub-backend-1  | INFO:     Application startup complete.
2025-07-16 04:38:34 gbstudio_hub-backend-1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
2025-07-16 04:38:37 gbstudio_hub-backend-1  | INFO:     192.168.176.1:60786 - "WebSocket /ws" [accepted]
2025-07-16 04:38:37 gbstudio_hub-backend-1  | INFO:     connection open
2025-07-16 04:39:17 gbstudio_hub-backend-1  | INFO:     Shutting down
2025-07-16 04:39:17 gbstudio_hub-backend-1  | INFO:     connection closed
2025-07-16 04:39:17 gbstudio_hub-backend-1  | INFO:     Waiting for application shutdown.
2025-07-16 04:39:17 gbstudio_hub-backend-1  | INFO:     Application shutdown complete.
2025-07-16 04:39:17 gbstudio_hub-backend-1  | INFO:     Finished server process [1]
2025-07-16 04:09:14 gbstudio_hub-comfyui-1  | /usr/local/bin/python: No module named uv
2025-07-16 04:09:14 gbstudio_hub-comfyui-1  | Failed to execute startup-script: /ComfyUI/custom_nodes/ComfyUI-Manager/prestartup_script.py / Command '['/usr/local/bin/python', '-m', 'uv', 'pip', 'freeze']' returned non-zero exit status 1.
2025-07-16 04:09:14 gbstudio_hub-comfyui-1  | 
2025-07-16 04:09:14 gbstudio_hub-comfyui-1  | Prestartup times for custom nodes:
2025-07-16 04:09:14 gbstudio_hub-comfyui-1  |    0.5 seconds (PRESTARTUP FAILED): /ComfyUI/custom_nodes/ComfyUI-Manager
2025-07-16 04:09:14 gbstudio_hub-comfyui-1  | 
2025-07-16 04:09:16 gbstudio_hub-comfyui-1  | Checkpoint files will always be loaded safely.
2025-07-16 04:09:16 gbstudio_hub-comfyui-1  | Total VRAM 7859 MB, total RAM 7859 MB
2025-07-16 04:09:16 gbstudio_hub-comfyui-1  | pytorch version: 2.7.1+cu126
2025-07-16 04:09:16 gbstudio_hub-comfyui-1  | Set vram state to: DISABLED
2025-07-16 04:09:16 gbstudio_hub-comfyui-1  | Device: cpu
2025-07-16 04:09:17 gbstudio_hub-comfyui-1  | Using sub quadratic optimization for attention, if you have memory or speed issues try using: --use-split-cross-attention
2025-07-16 04:09:20 gbstudio_hub-comfyui-1  | Python version: 3.11.13 (main, Jul  1 2025, 02:42:16) [GCC 12.2.0]
2025-07-16 04:09:20 gbstudio_hub-comfyui-1  | ComfyUI version: 0.3.44
2025-07-16 04:09:20 gbstudio_hub-comfyui-1  | ComfyUI frontend version: 1.23.4
2025-07-16 04:09:20 gbstudio_hub-comfyui-1  | [Prompt Server] web root: /usr/local/lib/python3.11/site-packages/comfyui_frontend_package/static
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | Traceback (most recent call last):
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |   File "/ComfyUI/nodes.py", line 2124, in load_custom_node
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |     module_spec.loader.exec_module(module)
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |   File "/ComfyUI/custom_nodes/ComfyUI-Image-Filters/__init__.py", line 1, in <module>
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |     from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |   File "/ComfyUI/custom_nodes/ComfyUI-Image-Filters/nodes.py", line 6, in <module>
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |     import cv2
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | ModuleNotFoundError: No module named 'cv2'
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | 
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | Cannot import /ComfyUI/custom_nodes/ComfyUI-Image-Filters module for custom nodes: No module named 'cv2'
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | Traceback (most recent call last):
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |   File "/ComfyUI/nodes.py", line 2124, in load_custom_node
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |     module_spec.loader.exec_module(module)
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |   File "/ComfyUI/custom_nodes/ComfyUI-Manager/__init__.py", line 12, in <module>
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |     import manager_server  # noqa: F401
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |     ^^^^^^^^^^^^^^^^^^^^^
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |   File "/ComfyUI/custom_nodes/ComfyUI-Manager/glob/manager_server.py", line 13, in <module>
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |     import git
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | ModuleNotFoundError: No module named 'git'
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | 
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | Cannot import /ComfyUI/custom_nodes/ComfyUI-Manager module for custom nodes: No module named 'git'
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | 
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | Import times for custom nodes:
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |    0.0 seconds: /ComfyUI/custom_nodes/websocket_image_save.py
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |    0.0 seconds (IMPORT FAILED): /ComfyUI/custom_nodes/ComfyUI-Manager
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  |    0.0 seconds (IMPORT FAILED): /ComfyUI/custom_nodes/ComfyUI-Image-Filters
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | 
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | Context impl SQLiteImpl.
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | Will assume non-transactional DDL.
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | No target revision found.
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | Starting server
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | 
2025-07-16 04:09:22 gbstudio_hub-comfyui-1  | To see the GUI go to: http://0.0.0.0:8188
2025-07-16 04:39:19 gbstudio_hub-backend-1  | INFO:     Started server process [1]
2025-07-16 04:39:19 gbstudio_hub-backend-1  | INFO:     Waiting for application startup.
2025-07-16 04:39:19 gbstudio_hub-backend-1  | 2025-07-16 08:39:19,417 - INFO - Database initialized successfully.
2025-07-16 04:39:19 gbstudio_hub-backend-1  | 2025-07-16 08:39:19,418 - INFO - Pixel art workflow is available at /ComfyUI/workflows/workflow_pixel_art.json
2025-07-16 04:39:19 gbstudio_hub-backend-1  | INFO:     Application startup complete.
2025-07-16 04:39:19 gbstudio_hub-backend-1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
2025-07-16 04:39:22 gbstudio_hub-backend-1  | INFO:     192.168.176.1:60790 - "WebSocket /ws" [accepted]
2025-07-16 04:39:22 gbstudio_hub-backend-1  | INFO:     connection open
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | time=2025-07-16T08:39:28.820Z level=INFO source=server.go:135 msg="system memory" total="7.7 GiB" free="6.5 GiB" free_swap="730.9 MiB"
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | time=2025-07-16T08:39:28.821Z level=INFO source=server.go:175 msg=offload library=cpu layers.requested=-1 layers.model=33 layers.offload=0 layers.split="" memory.available="[6.5 GiB]" memory.gpu_overhead="0 B" memory.required.full="5.8 GiB" memory.required.partial="0 B" memory.required.kv="1.0 GiB" memory.required.allocations="[5.8 GiB]" memory.weights.total="4.1 GiB" memory.weights.repeating="3.7 GiB" memory.weights.nonrepeating="411.0 MiB" memory.graph.full="560.0 MiB" memory.graph.partial="677.5 MiB"
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: loaded meta data with 22 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-6a0746a1ec1aef3e7ec53868f220ff6e389f6f8ef87a01d77c96807de94ca2aa (version GGUF V3 (latest))
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv   0:                       general.architecture str              = llama
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv   1:                               general.name str              = Meta-Llama-3-8B-Instruct
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv   2:                          llama.block_count u32              = 32
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv   3:                       llama.context_length u32              = 8192
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv   6:                 llama.attention.head_count u32              = 32
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv   7:              llama.attention.head_count_kv u32              = 8
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv   8:                       llama.rope.freq_base f32              = 500000.000000
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv  10:                          general.file_type u32              = 2
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv  11:                           llama.vocab_size u32              = 128256
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv  12:                 llama.rope.dimension_count u32              = 128
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv  13:                       tokenizer.ggml.model str              = gpt2
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv  14:                         tokenizer.ggml.pre str              = llama-bpe
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv  15:                      tokenizer.ggml.tokens arr[str,128256]  = ["!", "\"", "#", "$", "%", "&", "'", ...
2025-07-16 04:39:28 gbstudio_hub-ollama-1   | llama_model_loader: - kv  16:                  tokenizer.ggml.token_type arr[i32,128256]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  17:                      tokenizer.ggml.merges arr[str,280147]  = ["Ġ Ġ", "Ġ ĠĠĠ", "ĠĠ ĠĠ", "...
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  18:                tokenizer.ggml.bos_token_id u32              = 128000
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  19:                tokenizer.ggml.eos_token_id u32              = 128009
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  20:                    tokenizer.chat_template str              = {% set loop_messages = messages %}{% ...
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  21:               general.quantization_version u32              = 2
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - type  f32:   65 tensors
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - type q4_0:  225 tensors
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - type q6_K:    1 tensors
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: file format = GGUF V3 (latest)
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: file type   = Q4_0
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: file size   = 4.33 GiB (4.64 BPW) 
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | load: special tokens cache size = 256
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | load: token to piece cache size = 0.8000 MB
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: arch             = llama
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: vocab_only       = 1
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: model type       = ?B
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: model params     = 8.03 B
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: general.name     = Meta-Llama-3-8B-Instruct
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: vocab type       = BPE
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: n_vocab          = 128256
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: n_merges         = 280147
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: BOS token        = 128000 '<|begin_of_text|>'
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: EOS token        = 128009 '<|eot_id|>'
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: EOT token        = 128009 '<|eot_id|>'
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: LF token         = 198 'Ċ'
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: EOG token        = 128009 '<|eot_id|>'
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: max token length = 256
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_load: vocab only - skipping tensors
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | time=2025-07-16T08:39:29.389Z level=INFO source=server.go:438 msg="starting llama server" cmd="/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-6a0746a1ec1aef3e7ec53868f220ff6e389f6f8ef87a01d77c96807de94ca2aa --ctx-size 8192 --batch-size 512 --threads 4 --no-mmap --parallel 2 --port 43963"
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | time=2025-07-16T08:39:29.391Z level=INFO source=sched.go:483 msg="loaded runners" count=1
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | time=2025-07-16T08:39:29.391Z level=INFO source=server.go:598 msg="waiting for llama runner to start responding"
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | time=2025-07-16T08:39:29.392Z level=INFO source=server.go:632 msg="waiting for server to become available" status="llm server not responding"
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | time=2025-07-16T08:39:29.433Z level=INFO source=runner.go:815 msg="starting go runner"
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | load_backend: loaded CPU backend from /usr/lib/ollama/libggml-cpu-haswell.so
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | time=2025-07-16T08:39:29.463Z level=INFO source=ggml.go:104 msg=system CPU.0.SSE3=1 CPU.0.SSSE3=1 CPU.0.AVX=1 CPU.0.AVX2=1 CPU.0.F16C=1 CPU.0.FMA=1 CPU.0.BMI2=1 CPU.0.LLAMAFILE=1 CPU.1.LLAMAFILE=1 compiler=cgo(gcc)
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | time=2025-07-16T08:39:29.472Z level=INFO source=runner.go:874 msg="Server listening on 127.0.0.1:43963"
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: loaded meta data with 22 key-value pairs and 291 tensors from /root/.ollama/models/blobs/sha256-6a0746a1ec1aef3e7ec53868f220ff6e389f6f8ef87a01d77c96807de94ca2aa (version GGUF V3 (latest))
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv   0:                       general.architecture str              = llama
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv   1:                               general.name str              = Meta-Llama-3-8B-Instruct
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv   2:                          llama.block_count u32              = 32
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv   3:                       llama.context_length u32              = 8192
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv   4:                     llama.embedding_length u32              = 4096
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv   6:                 llama.attention.head_count u32              = 32
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv   7:              llama.attention.head_count_kv u32              = 8
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv   8:                       llama.rope.freq_base f32              = 500000.000000
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  10:                          general.file_type u32              = 2
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  11:                           llama.vocab_size u32              = 128256
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  12:                 llama.rope.dimension_count u32              = 128
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  13:                       tokenizer.ggml.model str              = gpt2
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  14:                         tokenizer.ggml.pre str              = llama-bpe
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  15:                      tokenizer.ggml.tokens arr[str,128256]  = ["!", "\"", "#", "$", "%", "&", "'", ...
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  16:                  tokenizer.ggml.token_type arr[i32,128256]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | time=2025-07-16T08:39:29.644Z level=INFO source=server.go:632 msg="waiting for server to become available" status="llm server loading model"
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  17:                      tokenizer.ggml.merges arr[str,280147]  = ["Ġ Ġ", "Ġ ĠĠĠ", "ĠĠ ĠĠ", "...
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  18:                tokenizer.ggml.bos_token_id u32              = 128000
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  19:                tokenizer.ggml.eos_token_id u32              = 128009
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  20:                    tokenizer.chat_template str              = {% set loop_messages = messages %}{% ...
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - kv  21:               general.quantization_version u32              = 2
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - type  f32:   65 tensors
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - type q4_0:  225 tensors
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | llama_model_loader: - type q6_K:    1 tensors
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: file format = GGUF V3 (latest)
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: file type   = Q4_0
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | print_info: file size   = 4.33 GiB (4.64 BPW) 
2025-07-16 04:39:29 gbstudio_hub-ollama-1   | load: special tokens cache size = 256
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | load: token to piece cache size = 0.8000 MB
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: arch             = llama
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: vocab_only       = 0
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_ctx_train      = 8192
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_embd           = 4096
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_layer          = 32
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_head           = 32
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_head_kv        = 8
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_rot            = 128
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_swa            = 0
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_swa_pattern    = 1
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_embd_head_k    = 128
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_embd_head_v    = 128
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_gqa            = 4
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_embd_k_gqa     = 1024
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_embd_v_gqa     = 1024
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: f_norm_eps       = 0.0e+00
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: f_norm_rms_eps   = 1.0e-05
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: f_clamp_kqv      = 0.0e+00
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: f_max_alibi_bias = 0.0e+00
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: f_logit_scale    = 0.0e+00
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: f_attn_scale     = 0.0e+00
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_ff             = 14336
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_expert         = 0
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_expert_used    = 0
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: causal attn      = 1
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: pooling type     = 0
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: rope type        = 0
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: rope scaling     = linear
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: freq_base_train  = 500000.0
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: freq_scale_train = 1
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_ctx_orig_yarn  = 8192
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: rope_finetuned   = unknown
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: ssm_d_conv       = 0
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: ssm_d_inner      = 0
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: ssm_d_state      = 0
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: ssm_dt_rank      = 0
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: ssm_dt_b_c_rms   = 0
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: model type       = 8B
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: model params     = 8.03 B
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: general.name     = Meta-Llama-3-8B-Instruct
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: vocab type       = BPE
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_vocab          = 128256
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: n_merges         = 280147
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: BOS token        = 128000 '<|begin_of_text|>'
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: EOS token        = 128009 '<|eot_id|>'
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: EOT token        = 128009 '<|eot_id|>'
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: LF token         = 198 'Ċ'
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: EOG token        = 128009 '<|eot_id|>'
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | print_info: max token length = 256
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | load_tensors: loading model tensors, this can take a while... (mmap = false)
2025-07-16 04:39:30 gbstudio_hub-ollama-1   | load_tensors:          CPU model buffer size =  4437.80 MiB
2025-07-16 04:40:18 gbstudio_hub-ollama-1   | llama_context: constructing llama_context
2025-07-16 04:40:18 gbstudio_hub-ollama-1   | llama_context: n_seq_max     = 2
2025-07-16 04:40:18 gbstudio_hub-ollama-1   | llama_context: n_ctx         = 8192
2025-07-16 04:40:18 gbstudio_hub-ollama-1   | llama_context: n_ctx_per_seq = 4096
2025-07-16 04:40:18 gbstudio_hub-ollama-1   | llama_context: n_batch       = 1024
2025-07-16 04:40:18 gbstudio_hub-ollama-1   | llama_context: n_ubatch      = 512
2025-07-16 04:40:18 gbstudio_hub-ollama-1   | llama_context: causal_attn   = 1
2025-07-16 04:40:18 gbstudio_hub-ollama-1   | llama_context: flash_attn    = 0
2025-07-16 04:40:18 gbstudio_hub-ollama-1   | llama_context: freq_base     = 500000.0
2025-07-16 04:40:18 gbstudio_hub-ollama-1   | llama_context: freq_scale    = 1
2025-07-16 04:40:18 gbstudio_hub-ollama-1   | llama_context: n_ctx_per_seq (4096) < n_ctx_train (8192) -- the full capacity of the model will not be utilized
2025-07-16 04:40:18 gbstudio_hub-ollama-1   | llama_context:        CPU  output buffer size =     1.01 MiB
2025-07-16 04:40:18 gbstudio_hub-ollama-1   | llama_kv_cache_unified: kv_size = 8192, type_k = 'f16', type_v = 'f16', n_layer = 32, can_shift = 1, padding = 32
2025-07-16 04:40:20 gbstudio_hub-ollama-1   | llama_kv_cache_unified:        CPU KV buffer size =  1024.00 MiB
2025-07-16 04:40:20 gbstudio_hub-ollama-1   | llama_kv_cache_unified: KV self size  = 1024.00 MiB, K (f16):  512.00 MiB, V (f16):  512.00 MiB
2025-07-16 04:40:20 gbstudio_hub-ollama-1   | llama_context:        CPU compute buffer size =   560.01 MiB
2025-07-16 04:40:20 gbstudio_hub-ollama-1   | llama_context: graph nodes  = 1094
2025-07-16 04:40:20 gbstudio_hub-ollama-1   | llama_context: graph splits = 1
2025-07-16 04:40:20 gbstudio_hub-ollama-1   | time=2025-07-16T08:40:20.226Z level=INFO source=server.go:637 msg="llama runner started in 50.84 seconds"
2025-07-16 04:41:42 gbstudio_hub-ollama-1   | [GIN] 2025/07/16 - 08:41:42 | 200 |         2m14s |   192.168.176.4 | POST     "/api/generate"
2025-07-16 04:41:42 gbstudio_hub-backend-1  | 2025-07-16 08:41:42,810 - INFO - Art agent response: workflow=workflow_pixel_art.json, asset_type=sprite, prompt=Create a charming 16x16 pixel art sprite of a friendly shopkeeper with a big, bushy brown mustache, wearing a white apron and a warm smile. The shopkeeper's face should be round and endearing, with bright blue eyes and a few wrinkles around the eyes. Hair is light brown and messy, sticking out from under the apron. Mustache should be the focal point, with thick curls at the ends. Shopkeeper should have a gentle, welcoming aura.
2025-07-16 04:41:42 gbstudio_hub-backend-1  | 2025-07-16 08:41:42,811 - INFO - Starting generation task: Create a sprite for a friendly shopkeeper with a big mustache with workflow workflow_pixel_art.json
2025-07-16 04:41:42 gbstudio_hub-backend-1  | 2025-07-16 08:41:42,832 - INFO - Attempting to log chat message: Create a sprite for a friendly shopkeeper with a big mustache
2025-07-16 04:41:42 gbstudio_hub-backend-1  | 2025-07-16 08:41:42,847 - INFO - Successfully logged chat message.
2025-07-16 04:41:42 gbstudio_hub-backend-1  | 2025-07-16 08:41:42,850 - INFO - Logged creation of asset 'Create a sprite for a friendly shopkeeper with a big mustache' with ID 1
2025-07-16 04:41:42 gbstudio_hub-comfyui-1  | got prompt
2025-07-16 04:41:42 gbstudio_hub-comfyui-1  | Failed to validate prompt for output 9:
2025-07-16 04:41:42 gbstudio_hub-comfyui-1  | * CheckpointLoaderSimple 4:
2025-07-16 04:41:42 gbstudio_hub-comfyui-1  |   - Value not in list: ckpt_name: 'v1-5-pruned-emaonly.safetensors' not in ['sd_xl_base_1.0.safetensors']
2025-07-16 04:41:42 gbstudio_hub-comfyui-1  | * LoraLoader 10:
2025-07-16 04:41:42 gbstudio_hub-comfyui-1  |   - Value not in list: lora_name: 'pixel-art-lora.safetensors' not in ['pixelart.safetensors']
2025-07-16 04:41:42 gbstudio_hub-comfyui-1  | Output will be ignored
2025-07-16 04:41:42 gbstudio_hub-comfyui-1  | invalid prompt: {'type': 'prompt_outputs_failed_validation', 'message': 'Prompt outputs failed validation', 'details': '', 'extra_info': {}}
2025-07-16 04:41:42 gbstudio_hub-backend-1  | 2025-07-16 08:41:42,905 - ERROR - Generation task failed for asset 1: ComfyUI Error: {"error": {"type": "prompt_outputs_failed_validation", "message": "Prompt outputs failed validation", "details": "", "extra_info": {}}, "node_errors": {"4": {"errors": [{"type": "value_not_in_list", "message": "Value not in list", "details": "ckpt_name: 'v1-5-pruned-emaonly.safetensors' not in ['sd_xl_base_1.0.safetensors']", "extra_info": {"input_name": "ckpt_name", "input_config": [["sd_xl_base_1.0.safetensors"], {"tooltip": "The name of the checkpoint (model) to load."}], "received_value": "v1-5-pruned-emaonly.safetensors"}}], "dependent_outputs": ["9"], "class_type": "CheckpointLoaderSimple"}, "10": {"errors": [{"type": "value_not_in_list", "message": "Value not in list", "details": "lora_name: 'pixel-art-lora.safetensors' not in ['pixelart.safetensors']", "extra_info": {"input_name": "lora_name", "input_config": [["pixelart.safetensors"], {"tooltip": "The name of the LoRA."}], "received_value": "pixel-art-lora.safetensors"}}], "dependent_outputs": ["9"], "class_type": "LoraLoader"}}}
2025-07-16 04:45:15 gbstudio_hub-backend-1  | INFO:     192.168.176.1:57042 - "GET / HTTP/1.1" 200 OK
2025-07-16 04:45:15 gbstudio_hub-backend-1  | INFO:     connection closed
2025-07-16 04:45:15 gbstudio_hub-backend-1  | INFO:     192.168.176.1:57052 - "GET /static/js/app.js HTTP/1.1" 304 Not Modified
2025-07-16 04:45:15 gbstudio_hub-backend-1  | INFO:     192.168.176.1:57042 - "GET /static/css/main.css HTTP/1.1" 304 Not Modified
2025-07-16 04:45:15 gbstudio_hub-backend-1  | INFO:     192.168.176.1:57056 - "WebSocket /ws" [accepted]
2025-07-16 04:45:15 gbstudio_hub-backend-1  | INFO:     connection open
2025-07-16 04:45:15 gbstudio_hub-backend-1  | INFO:     192.168.176.1:57042 - "GET /favicon.ico HTTP/1.1" 404 Not Found
2025-07-16 04:48:21 gbstudio_hub-ollama-1   | [GIN] 2025/07/16 - 08:48:21 | 200 |         2m32s |   192.168.176.4 | POST     "/api/generate"
2025-07-16 04:48:21 gbstudio_hub-backend-1  | INFO:     192.168.176.1:56454 - "POST /api/v1/chat/PM HTTP/1.1" 200 OK
2025-07-16 04:48:21 gbstudio_hub-backend-1  | 2025-07-16 08:48:21,566 - INFO - Attempting to log chat message: Jason Voorhees idle animation (four frames,) breathing heavily with a machete at his side. Game Boy Color compliant.
2025-07-16 04:48:21 gbstudio_hub-backend-1  | 2025-07-16 08:48:21,593 - INFO - Successfully logged chat message.
2025-07-16 04:52:00 gbstudio_hub-ollama-1   | [GIN] 2025/07/16 - 08:52:00 | 200 |         2m53s |   192.168.176.4 | POST     "/api/generate"
2025-07-16 04:52:00 gbstudio_hub-backend-1  | 2025-07-16 08:52:00,809 - INFO - Art agent response: workflow=workflow_pixel_art.json, asset_type=sprite, prompt={'type': 'pixel art', 'scene': 'Jason Voorhees standing with machete by his side, breathing heavily', 'spritesheet': 8, 'frames': 4, 'colors': ['#000000', '#FF9900'], 'composition': {'jason': {'pose': 'standing', 'orientation': 'frontal', 'expression': 'menacing'}, 'machete': {'position': "by jason's side", 'angle': 'horizontal'}, 'breathing': {'style': 'heavy breathing', 'direction': 'exhaling'}}}
2025-07-16 04:52:00 gbstudio_hub-backend-1  | 2025-07-16 08:52:00,809 - INFO - Starting generation task: {
2025-07-16 04:52:00 gbstudio_hub-backend-1  |   "department": "Art",
2025-07-16 04:52:00 gbstudio_hub-backend-1  |   "task_description": "Create four 8x8 pixel art frames for an idle animation of Jason Voorhees, depicting him standing with a machete by his side and breathing heavily. Ensure the design is game boy color compliant and captures Jason's menacing presence. The animation should be simple yet eerie."
2025-07-16 04:52:00 gbstudio_hub-backend-1  | } with workflow workflow_pixel_art.json
2025-07-16 04:52:00 gbstudio_hub-backend-1  | INFO:     192.168.176.1:61314 - "POST /api/v1/chat/Art HTTP/1.1" 200 OK
2025-07-16 04:52:00 gbstudio_hub-backend-1  | 2025-07-16 08:52:00,811 - INFO - Attempting to log chat message: {
2025-07-16 04:52:00 gbstudio_hub-backend-1  |   "department": "Art",
2025-07-16 04:52:00 gbstudio_hub-backend-1  |   "task_description": "Create four 8x8 pixel art frames for an idle animation of Jason Voorhees, depicting him standing with a machete by his side and breathing heavily. Ensure the design is game boy color compliant and captures Jason's menacing presence. The animation should be simple yet eerie."
2025-07-16 04:52:00 gbstudio_hub-backend-1  | }
2025-07-16 04:52:00 gbstudio_hub-backend-1  | 2025-07-16 08:52:00,822 - INFO - Successfully logged chat message.
2025-07-16 04:52:00 gbstudio_hub-backend-1  | 2025-07-16 08:52:00,824 - ERROR - Failed to log asset creation for '{
2025-07-16 04:52:00 gbstudio_hub-backend-1  |   "department": "Art",
2025-07-16 04:52:00 gbstudio_hub-backend-1  |   "task_description": "Create four 8x8 pixel art frames for an idle animation of Jason Voorhees, depicting him standing with a machete by his side and breathing heavily. Ensure the design is game boy color compliant and captures Jason's menacing presence. The animation should be simple yet eerie."
2025-07-16 04:52:00 gbstudio_hub-backend-1  | }': Error binding parameter 3 - probably unsupported type.
2025-07-16 04:52:00 gbstudio_hub-backend-1  | 2025-07-16 08:52:00,825 - ERROR - Generation task failed for asset -1: Failed to log asset creation in the database.

