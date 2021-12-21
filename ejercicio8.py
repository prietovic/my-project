import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAlerts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Users\\99GU3945\\workspaces\\test-lab\\chromedriver.exe')

    def test_alert(self):
        #driver = webdriver.Chrome('C:\\Users\\99GU3945\\workspaces\\test-lab\\chromedriver.exe')
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        alertButton = self.driver.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(1) > button")
        alertButton.click()

        alert = self.driver.switch_to.alert
        alert.accept()

        result = self.driver.find_element(By.ID,"result")
        result_text = result.text

        assert result_text == "You successfully clicked an alert"

        self.driver.quit()

    def test_confirm_accept(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        confirmButton = self.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(2) > button")
        confirmButton.click()

        alert = self.driver.switch_to.alert
        alert.accept()

        result = self.driver.find_element(By.ID, "result")
        result_text = result.text

        assert result_text == "You clicked: Ok"

        self.driver.quit()

    def test_confirm_cancel(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        confirmButton = self.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(2) > button")
        confirmButton.click()

        alert = self.driver.switch_to.alert
        alert.dismiss()

        result = self.driver.find_element(By.ID, "result")
        result_text = result.text

        assert result_text == "You clicked: Cancel"

        self.driver.quit()

    def test_js_prompt(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        prompt_button = self.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(3) > button")
        prompt_button.click()

        alert = self.driver.switch_to.alert
        a = "asdf"
        alert.send_keys(a)
        alert.accept()

        result = self.driver.find_element(By.ID, "result")
        result_text = result.text

        assert result_text == "You entered: " + a
        assert a in result_text

        self.driver.quit()
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    # unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # en jupyter solo funciona poniéndolo así