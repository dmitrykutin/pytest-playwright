import threading
import uvicorn


# this method creates a thread to run the FastAPI server,
# so that it doesn't block the main thread where the tests are running.
def run_server(app, port):
    config = uvicorn.Config(app, host="0.0.0.0", port=port, log_level="warning")
    server = uvicorn.Server(config)
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    return server
