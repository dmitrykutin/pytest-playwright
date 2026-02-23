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
- src/clients folder - for API client to work with in api-tests
- src/pages folder - for page-objects classes to work with ui-tests
- static/index.html - just static html file to use in ui tests (click on buttons etc.)
- tests/api - tests to test api
- tests/ui - tests to test ui
- conftest.py - file with a lot of things - fixtures, run the ui web page and api endpoint
- requirements.txt - file with libs you need to install to use the project

