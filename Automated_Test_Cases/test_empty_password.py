import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestEmptyPassword(unittest.TestCase):
    def setUp(self):
    
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)

    def test_empty_password(self):
        driver = self.driver

      
        driver.find_element(By.NAME, "username").send_keys("Admin")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        required_error = driver.find_element(By.XPATH, "//span[text()='Required']")
        self.assertTrue(required_error.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
