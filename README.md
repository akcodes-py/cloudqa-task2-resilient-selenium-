# Task 2: AI-driven browser test runner (Python + Selenium + Groq)

Accepts a starting URL and a plain-English test. Groq proposes one browser action at a time from a current page snapshot; Selenium performs it and **independently verifies** the final assertion. No selectors or flow are hard-coded to PHPTRAVELS.

## Windows setup

Prerequisites: Python 3.10+ and Chrome. The basic visible-text check requires no AI provider or API key; Groq is an optional planner for multi-step flows.

```powershell
cd cloudqa-task2-ai-test-runner
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python ai_selenium_runner.py --url 'https://phptravels.com/demo' --test 'Verify the demo page has a Get demo access section' --headless
```

The above simple PHPTRAVELS check runs without any AI API. Without a key, the runner checks a plainly stated phrase in visible browser text; it does not claim to autonomously perform logins or arbitrary actions. To optionally enable AI-planned flows using Groq, set `$env:GROQ_API_KEY = 'your-key'` in that same PowerShell terminal. Never commit or record the key. Groq model availability is account-dependent.

To show Chrome during the recording, omit `--headless`. If PowerShell blocks activation, use `.\.venv\Scripts\python.exe` instead. Selenium Manager downloads ChromeDriver if needed.

Optional Groq-only second-site login example (public SauceDemo sample credentials; do **not** use real passwords on the CLI):

```powershell
$env:TEST_CONTEXT = 'Username standard_user, password secret_sauce'
python ai_selenium_runner.py --url 'https://www.saucedemo.com/' --test 'Log in and verify Products is displayed' --headless
```

`GROQ_MODEL` overrides the default `llama-3.3-70b-versatile`; availability and rate limits are subject to your Groq account. `--max-steps` defaults to 12. `python -m unittest -v` runs local checks without a Groq key. The tool returns exit code 0 for PASS, 1 for FAIL; a failure screenshot goes to `artifacts/failure.png`.

## Approach and limitations

In optional AI mode, the snapshot contains current URL, headings, visible body text, and up to 120 visible interactive controls with short-lived numeric IDs. After every action, it observes and replans. Only an allowlisted action can be executed, and a model-suggested assertion must actually succeed in the browser. The runner does not accept model text that merely says “pass”. Without a key, it only checks the requested visible phrase and does not attempt a login.

This is a prototype: an LLM can choose a weak assertion, and visible-text assertions do not establish account identity or server-side correctness. Inspect the trace. Captchas, anti-bot checks, iframes, shadow roots, canvas/custom widgets and ambiguous flows may fail. The page snapshot and any supplied context are sent to Groq; do not use sensitive credentials or pages without permission. PHPTRAVELS currently requests demo credentials through a form; this example checks the public page without claiming to have those credentials. Details: `dicison.md`.

## Five-minute recording outline

1. Show Task 1 running on CloudQA and the scrambled local fixture.
2. Show this runner's PHPTRAVELS example, then the SauceDemo example with Chrome visible; hide the API key.
3. Show an intentionally false assertion producing FAIL, then summarize the limitations and decision notes.
