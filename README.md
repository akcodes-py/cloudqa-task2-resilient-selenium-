# Task 2: AI-driven browser test runner (Python + Selenium + Groq)

Accepts a starting URL and a plain-English test. Groq proposes one browser action at a time from a current page snapshot; Selenium performs it and **independently verifies** the final assertion. No selectors or flow are hard-coded to PHPTRAVELS.

## Windows setup

Prerequisites: Python 3.10+, Chrome, and a valid Groq API key. Groq is the plain-English test planner; Selenium drives Chrome and verifies the result.

```powershell
cd cloudqa-task2-ai-test-runner
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:GROQ_API_KEY = 'your-valid-groq-key'
python ai_selenium_runner.py --url 'https://phptravels.com/demo' --test 'Verify the demo page has a Get demo access section' --headless
```

`GROQ_API_KEY` is required for the plain-English planner. You can set it in the PowerShell session, or save it to a local `.env` file in this project directory (the file is git-ignored):

```text
GROQ_API_KEY=your-valid-groq-key
GROQ_MODEL=openai/gpt-oss-20b
```

Never commit the key or show it in the recording. If no key is set, a simple visible-text fallback is available, but it is **not** the full AI test-runner task and cannot carry out arbitrary instructions.

To show Chrome during the recording, omit `--headless`. If PowerShell blocks activation, use `.\.venv\Scripts\python.exe` instead. Selenium Manager downloads ChromeDriver if needed.

Second-site login example (public SauceDemo sample credentials; do **not** use real passwords on the CLI):

```powershell
$env:TEST_CONTEXT = 'Username standard_user, password secret_sauce'
python ai_selenium_runner.py --url 'https://www.saucedemo.com/' --test 'Log in and verify Products is displayed' --headless
```

`GROQ_MODEL` overrides the default `llama-3.3-70b-versatile`; availability and rate limits are subject to your Groq account. `--max-steps` defaults to 12. `python -m unittest -v` runs local checks without a Groq key. The tool returns exit code 0 for PASS, 1 for FAIL; a failure screenshot goes to `artifacts/failure.png`.

## Approach and limitations

The Groq planner receives the plain-English scenario, current URL/headings/visible text, up to 120 visible interactive controls, and action history. It chooses one allowlisted browser action at a time. Selenium performs the action and re-observes the page. A PASS requires a Selenium-verified visible-text or URL assertion; a model response saying “pass” is not enough. Without a key, the limited fallback only checks visible text and cannot autonomously follow new instructions.

This is a prototype: an LLM can choose a weak assertion, and visible-text assertions do not establish account identity or server-side correctness. Inspect the trace. Captchas, anti-bot checks, iframes, shadow roots, canvas/custom widgets and ambiguous flows may fail. The page snapshot and any supplied context are sent to Groq; do not use sensitive credentials or pages without permission. PHPTRAVELS currently requests demo credentials through a form; this example checks the public page without claiming to have those credentials. Details: `dicison.md`.

## Five-minute recording outline

1. Show Task 1 running on CloudQA and the scrambled local fixture.
2. Show this runner's PHPTRAVELS example, then the SauceDemo example with Chrome visible; hide the API key.
3. Show an intentionally false assertion producing FAIL, then summarize the limitations and decision notes.
