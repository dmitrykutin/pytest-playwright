from fastapi import Depends, FastAPI, Query
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from pydantic import BaseModel
from src.db.connectDB import Database


# Pydantic model for user creation
# we need this to successfully parse the request body
# when we send POST request to /users endpoint (see create_user function below)
class User(BaseModel):
    first_name: str
    last_name: str


# method to get connection to db for endpoints that need it (like create_user)
def get_db():
    db = Database()
    try:
        yield db
    finally:
        db.close()


# method to create the FastAPI app - static and API endpoints
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

    # Create an API endpoint in localhost:8000/users
    # that accepts POST request with JSON body containing "first_name" and "last_name"
    @app.post("/users")
    def create_user(user: User, db: Database = Depends(get_db)):
        # here insert new row to the users table with received data
        # and save the id from last row in users table
        # look at insert_user method in connectDB.py
        user_id = db.insert_user(user.first_name, user.last_name)
        # here return a JSON response
        return {
            "message": "User created",
            "data": {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "id": user_id,
            },
        }

    return app
