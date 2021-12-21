import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAlerts(unittest.TestCase):

   def setUp(self):
        self.driver = webdriver.Chrome('C:\\Users\\99GU3945\\workspaces\\test-lab\\chromedriver.exe')

   def test_new_window(self):
        self.driver.get("https://the-internet.herokuapp.com/windows")
        link = self.driver.find_element(By.CSS_SELECTOR,"#content > div > a")
        link.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)

        text_object = self.driver.find_element(By.CSS_SELECTOR,"body > div > h3")
        assert text_object == "New Window"

        #self.driver.quit()


   def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    # unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # en jupyter solo funciona poniéndolo así