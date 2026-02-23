import pytest
import threading
import uvicorn
import time
from src.clients.api_main import APIClient
from src.pages.main_page import MainPage
from playwright.sync_api import sync_playwright
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# ----------------------------
# Constants for the server. Will use it later when we start the server
# ----------------------------
BASE_URL_API = "http://localhost:8000"
BASE_URL = "http://localhost:8000/index.html"
PORT = 8000
DIRECTORY = "static"

# Create a FastAPI to work with it later
app = FastAPI()


# Mount the static file static/index.html to the root URL (http://localhost:8000/index.html)
# to have access to it in tests
app.mount(
    "/index.html", StaticFiles(directory=Path(DIRECTORY), html=True), name="static"
)


# Create a API endpoint in localhost:8000/api/hello
# that returns a simple JSON response if we make GET request to it
@app.get("/api/hello")
def hello():
    return {"message": "hello"}


# ----------------------------
# 1️⃣ Run server in background thread
# ----------------------------


# scope = "session" means the fixture will be run once a session for all tests.
# autouse=True means that the fixture will be automatically used by all tests,
# you don't need to add it as a parameter to your test functions.
@pytest.fixture(scope="session", autouse=True)
def start_server():
    # Use uvicorn to run the FastAPI app in background thread
    # "background thread" means that it will run in parallel with the tests,
    # and it won't block the execution of the tests.

    # first create a config for uvicorn with our app
    # ("app" and "PORT" were created before), host, port, and log level
    config = uvicorn.Config(app, host="0.0.0.0", port=PORT, log_level="warning")

    # then create a server with that config
    server = uvicorn.Server(config)

    # create a thread to run the server,
    # and set daemon=True so that it will automatically close
    # when the main thread (the tests) finishes
    thread = threading.Thread(target=server.run, daemon=True)
    # start the server thread
    thread.start()
    # wait a little to start the server
    time.sleep(0.5)
    # return control to the tests, and when all tests are done,
    # it returns back here, and it stops the server
    yield
    # stop the server
    server.should_exit = True


# ----------------------------
# 2️⃣ Browser options, command line args, use like:
# pytest --browser=chromium (but it's default, you don't need to use it) or
# pytest --browser=firefox or
# pytest --browser=webkit
# ----------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to use: chromium, firefox, or webkit",
    )


# This fixture will be used by the 'browser' fixture to determine which browser to launch
@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser")


# ----------------------------
# 3️⃣ Playwright browser.
# ----------------------------
@pytest.fixture(scope="session")
def browser(browser_name):
    # Use sync_playwright to launch the browser based on the command line argument (--browser) defined before.
    # It will launch the browser in headed mode (headless=False) so it opens the browser.
    # 'with' means that it will close the browser after all tests are done
    with sync_playwright() as p:
        # 'browser_launcher' allows to launch the browser based on the browser_name variable (chromium, firefox, or webkit)
        # 'p' means the playwright instance we got from sync_playwright.
        # so browser_launcher = p.firefox or others
        browser_launcher = getattr(p, browser_name)
        # python runs the browser and returns the browser instance to 'browser'
        browser = browser_launcher.launch(headless=False)
        # 'yield' means that it will return the browser instance to the tests,
        # and when all tests are done, it will return back here and close the browser.
        yield browser
        browser.close()


# ----------------------------
# 4️⃣ Page. It's opened a page in browser for each test, and closed after the test is done.
# ----------------------------
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    context.close()


# ----------------------------
# 5️⃣ Page Object. We create an instance of MainPage for each test,
# and it uses the 'page' fixture.
# If you have more page objects, you can create more fixtures
# and use it like def login_test(main_page, login_page): and use methods from both page objects in the same test.
# ----------------------------
@pytest.fixture
def main_page(page):
    return MainPage(page)


@pytest.fixture
def api_client():
    return APIClient(BASE_URL_API)
