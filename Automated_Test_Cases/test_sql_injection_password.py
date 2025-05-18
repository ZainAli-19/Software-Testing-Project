import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSQLInjectionPassword(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)

    def test_sql_injection_password(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("' OR '1'='1")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        error = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'oxd-alert-content')]")
        ))

        self.assertTrue(error.is_displayed())
        print("SQL injection in password blocked. Error message:", error.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
