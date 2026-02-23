from fastapi import FastAPI, Query
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

    # Create an API endpoint in localhost:8000/api/data_type
    # if we send GET request to it with parameter "value=10" it should answer
    # {"data_type": "integer"}, the same for float and string
    @app.get("/api/data_type")
    def get_data(value: str = Query(...)):
        try:
            int(value)
            return {"data_type": "integer"}
        except ValueError:
            pass
        try:
            float(value)
            return {"data_type": "float"}
        except ValueError:
            pass
        return {"data_type": "string"}

    return app
