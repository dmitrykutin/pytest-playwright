from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

# method to create the FastAPI app - static and API endpoint


def create_app():

    # Constant for the server. Will use it later when we start the server
    DIRECTORY = "static"

    app = FastAPI()

    # Mount the static file static/index.html to the root URL (http://localhost:8000/index.html)
    # to have access to it in tests
    app.mount(
        "/index.html",
        StaticFiles(directory=Path(DIRECTORY), html=True),
        name="static",
    )

    # Create a API endpoint in localhost:8000/api/hello
    # that returns a simple JSON response if we make GET request to it
    @app.get("/api/hello")
    def hello():
        return {"message": "hello"}

    return app
