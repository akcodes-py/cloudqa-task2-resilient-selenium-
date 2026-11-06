# Task 2: AI-driven browser test runner (Python + Selenium + Groq)

Accepts a starting URL and a plain-English test. Groq proposes one browser action at a time from a current page snapshot; Selenium performs it and **independently verifies** the final assertion. No selectors or flow are hard-coded to PHPTRAVELS.

## Windows setup

Prerequisites: Python 3.10+, Chrome, internet access, and your own Groq API key.

```powershell
cd cloudqa-task2-ai-test-runner
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:GROQ_API_KEY = 'your-own-key'
python ai_selenium_runner.py --url 'https://phptravels.com/demo' --test 'Verify the demo page has a Get demo access section' --headless
```

`GROQ_API_KEY` is required for an AI-driven run. Create a key in your Groq account, then set it in the same PowerShell terminal with `$env:GROQ_API_KEY = 'gsk-...'`. Do not commit the key, paste it into a test JSON file, or share it in a recording. The runner checks for the environment variable and reports an error if it is missing.

To show Chrome during the recording, omit `--headless`. If PowerShell blocks activation, use `.\.venv\Scripts\python.exe` instead. Selenium Manager downloads ChromeDriver if needed.

Second website example (public SauceDemo sample credentials; do **not** use real passwords on the CLI):

```powershell
$env:TEST_CONTEXT = 'Username standard_user, password secret_sauce'
python ai_selenium_runner.py --url 'https://www.saucedemo.com/' --test 'Log in and verify Products is displayed' --headless
```

`GROQ_MODEL` overrides the default `llama-3.3-70b-versatile`; availability and rate limits are subject to your Groq account. `--max-steps` defaults to 12. `python -m unittest -v` runs local checks without a Groq key. The tool returns exit code 0 for PASS, 1 for FAIL; a failure screenshot goes to `artifacts/failure.png`.

## Approach and limitations

The snapshot contains current URL, headings, visible body text, and up to 120 visible interactive controls with short-lived numeric IDs. After every action, it observes and replans. Only an allowlisted action can be executed, and a model-suggested assertion must actually succeed in the browser. The runner does not accept model text that merely says “pass”.

This is a prototype: an LLM can choose a weak assertion, and visible-text assertions do not establish account identity or server-side correctness. Inspect the trace. Captchas, anti-bot checks, iframes, shadow roots, canvas/custom widgets and ambiguous flows may fail. The page snapshot and any supplied context are sent to Groq; do not use sensitive credentials or pages without permission. PHPTRAVELS currently requests demo credentials through a form; this example checks the public page without claiming to have those credentials. Details: `dicison.md`.

## Five-minute recording outline

1. Show Task 1 running on CloudQA and the scrambled local fixture.
2. Show this runner's PHPTRAVELS example, then the SauceDemo example with Chrome visible; hide the API key.
3. Show an intentionally false assertion producing FAIL, then summarize the limitations and decision notes.
