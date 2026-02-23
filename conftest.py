import pytest
import src.app.fastapi as fastapi
from src.clients.api_main import APIClient
from src.pages.main_page import MainPage
from playwright.sync_api import sync_playwright
from tests.utils.server import run_server

# ----------------------------
# Constants for the server. Will use it later when we start the server
# ----------------------------
BASE_URL_API = "http://localhost:8000"
BASE_URL = "http://localhost:8000/index.html"
PORT = 8000
DIRECTORY = "static"


# ----------------------------
# 1️ - it's a fixture ('fixture' means that it can be used in tests, and it will run before the test starts).
# Start the FastAPI server before running the tests, and stop it after all tests are done.
# We use 'session' scope so that it runs once for the whole test session, and
# ----------------------------
@pytest.fixture(scope="session", autouse=True)
def start_server():
    # fastapi.create_app() creates the FastAPI app for both - static and API endpoint
    app = fastapi.create_app()
    # run_server takes the FastAPI app and the port number and starts the server
    server = run_server(app, PORT)
    # yield means that it will return control to the tests.
    # but when tests are done, it will come back here and execute the code after (close the server).
    yield
    server.should_exit = True


# ----------------------------
# 2️ - Browser options, command line args, use like:
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
# 3️ - Playwright browser. Just run the browser.
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
# 4️ - Page. It's opened a page in browser for each test, and closed after the test is done.
# ----------------------------
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    context.close()


# ----------------------------
# 5 - Page Object. We create an instance of MainPage for each test,
# and it uses the 'page' fixture.
# If you have more page objects, you can create more fixtures
# and use it like def login_test(main_page, login_page): and use methods from both page objects in the same test.
# ----------------------------
@pytest.fixture
def main_page(page):
    return MainPage(page)


# it's like page object for API. We can use methods in src/clients/api_main.py in our tests
# look at tests/test_api.py for example of usage
@pytest.fixture
def api_client():
    return APIClient(BASE_URL_API)
