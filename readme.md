Test project using Playwright and pytest

By run "pytest" it runs local server with test web-page app/index.html and perform test-case tests/test_page.py

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
python -m pytest -q --browser=firefox
```

Notes
- The `run_server.py` script starts a local HTTP server on port 8000.
- If port 8000 is already in use, the fixture will use the existing server.

Files
- [conftest.py](conftest.py) — server auto-start and pytest configuration
- [requirements.txt](requirements.txt) — project dependencies
- [setup.ps1](setup.ps1) — Windows PowerShell setup script
- [setup.sh](setup.sh) — macOS / Linux setup script
