import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestEmptyUsername(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)

    def test_empty_username(self):
        driver = self.driver
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        required_error = driver.find_element(By.XPATH, "//span[text()='Required']")
        self.assertTrue(required_error.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()