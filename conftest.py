import pytest
import threading
import http.server
import socketserver
from pages.main_page import MainPage
from playwright.sync_api import sync_playwright

# ----------------------------
# Constants for the server
# ----------------------------
BASE_URL = "http://localhost:8000/index.html"
PORT = 8000
DIRECTORY = "app"


# ----------------------------
# 1️⃣ Run server in background thread
# ----------------------------
@pytest.fixture(scope="session", autouse=True)
def start_server():
    handler = http.server.SimpleHTTPRequestHandler

    def run_server():
        # Open directory and start server
        import os
        os.chdir(DIRECTORY)
        with socketserver.TCPServer(("", PORT), handler) as httpd:
            httpd.serve_forever()

    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()

    # take some time for the server to start
    import time
    time.sleep(0.5)

    yield  # the server will keep running in the background until all tests are done, 
    # then the daemon thread will exit automatically
    


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
    with sync_playwright() as p:
        browser_launcher = getattr(p, browser_name)
        browser = browser_launcher.launch(headless=False)
        yield browser
        browser.close()


# ----------------------------
# 4️⃣ Page. It's opened for each test, and closed after the test is done.
# ----------------------------
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    context.close()


# ----------------------------
# 5️⃣ Page Object. We create an instance of MainPage for each test, and it uses the 'page' fixture.
# ----------------------------
@pytest.fixture
def main_page(page):
    return MainPage(page)
