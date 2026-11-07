import unittest

from selenium import webdriver

from ai_selenium_runner import SNAPSHOT_JS, execute, validate_decision, validate_url


class PlanTests(unittest.TestCase):
    def test_reject_invalid_navigation(self):
        with self.assertRaises(ValueError):
            validate_url("javascript:alert(1)")

    def test_reject_unknown_action_and_invalid_element(self):
        state = {"elements": [{"id": 1}]}
        with self.assertRaises(ValueError):
            validate_decision({"action": "shell"}, state)
        with self.assertRaises(ValueError):
            validate_decision({"action": "click", "element_id": 10}, state)

    def test_validate_and_solve_simple_math_prompt(self):
        state = {"elements": [{"id": 3, "tag": "input", "type": "text"}]}
        decision = validate_decision({"action": "solve_math", "prompt": "5 + 5 =", "element_id": 3}, state)
        self.assertEqual(decision["prompt"], "5 + 5 =")
        self.assertIn("solve_math", __import__("ai_selenium_runner").ACTIONS)

    def test_browser_assertion_not_model_claim(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        with webdriver.Chrome(options=options) as driver:
            driver.get("data:text/html,<h1>Products</h1><button>Continue</button>")
            state = driver.execute_script(SNAPSHOT_JS)
            self.assertTrue(execute(driver, {"action": "assert_visible", "value": "Products"}, state))
            with self.assertRaises(AssertionError):
                execute(driver, {"action": "assert_visible", "value": "Dashboard"}, state)


if __name__ == "__main__":
    unittest.main()
