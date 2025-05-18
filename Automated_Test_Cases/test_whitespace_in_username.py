import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWhitespaceInUsername(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)

    def test_whitespace_in_username(self):
        driver = self.driver

        driver.find_element(By.NAME, "username").send_keys("   ")

        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        required_error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Required']"))
        )
        self.assertTrue(required_error.is_displayed(), "Expected 'Required' error not displayed for username.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
