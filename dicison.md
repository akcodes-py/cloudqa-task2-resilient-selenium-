# Decisions — Task 2

1. **Python + Selenium + Groq for Task 2:** Groq interprets the plain-English case and proposes actions; Selenium controls the browser and verifies assertions. `GROQ_API_KEY` is read from the environment, never embedded. A no-key phrase-check fallback is only for a limited local smoke check and is not a replacement for the AI task.
2. **Observe–decide–act:** Read a bounded DOM snapshot after each step and assign temporary element IDs. These IDs are only valid until the next observation. The model chooses a single allowlisted action, never arbitrary code.
3. **Browser-verified PASS:** Model output cannot directly mark a test passed. The runner verifies visible text or URL in Chrome. Action failures, invalid targets, and step limits fail.
4. **Generic across domains:** Neither selectors nor credentials are specific to PHPTRAVELS or SauceDemo; the two commands in the README are examples. PHPTRAVELS now requires a request for demo credentials, so the public example does not promise a login.
5. **Honest limitations:** No iframe/shadow traversal, and the model can still choose an insufficient assertion; CAPTCHA and external service quotas can prevent completion. Keep test cases specific and review results.

## Verified run

Ran the PHPTRAVELS public demo-page check using Groq `openai/gpt-oss-20b` and Selenium in headless Chrome. The model proposed a visible-text assertion; Selenium independently found `Get your demo access` and reported PASS. Three local unit tests passed. The API key is stored only in the ignored local `.env` and was not added to Git.
