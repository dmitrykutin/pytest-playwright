Test project using Playwright and pytest

By run "pytest" it runs:
- local server with test web-page app/index.html
- fastAPI endpoint
and performs test-cases at tests/ui/test_page.py and tests/api/test_hello_api.py

Requirements
- Python 3.10+
- Git

Quick setup (Windows PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install
python -m pytest -q
```

Quick setup (macOS / Linux)

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install
python -m pytest -q
```

Run tests with a different browser

```
python -m pytest --browser=firefox
or just try
pytest
```

Notes for files
- src/
  - clients/ folder - for API client to work with in api-tests
  - pages/ folder - for page-objects classes to work with ui-tests
  - app/
    - fastapi.py - create FastAPI app
- static/
  - index.html - just static html file to use in ui tests (click on buttons etc.)
- tests/
  - utils/
    - server.py - run the server in another thread (to not block main thread with tests)
  - api - tests to test api
  - ui - tests to test ui
    
- conftest.py - fixtures, run the server, open browser, open browser tab for each test, pytest_adoption (arguments for terminal)
- requirements.txt - file with libs you need to install to use the project

