# Decisions — Task 2

1. **Python + Selenium + Groq:** Matches the requested browser stack; uses `GROQ_API_KEY` instead of embedding a secret or pretending a free Groq account exists.
2. **Observe–decide–act:** Read a bounded DOM snapshot after each step and assign temporary element IDs. These IDs are only valid until the next observation. The model chooses a single allowlisted action, never arbitrary code.
3. **Browser-verified PASS:** Model output cannot directly mark a test passed. The runner verifies visible text or URL in Chrome. Action failures, invalid targets, and step limits fail.
4. **Generic across domains:** Neither selectors nor credentials are specific to PHPTRAVELS or SauceDemo; the two commands in the README are examples. PHPTRAVELS now requires a request for demo credentials, so the public example does not promise a login.
5. **Honest limitations:** No iframe/shadow traversal, and the model can still choose an insufficient assertion; CAPTCHA and external service quotas can prevent completion. Keep test cases specific and review results.
