import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCaseSensitiveUsername(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)

    def test_case_sensitive_username(self):
        driver = self.driver
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        wait = WebDriverWait(driver, 15)

        try:

            wait.until(EC.url_contains("dashboard"))

            dashboard_header = wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[1]/div[1]/span/h6")
                )
            )

            self.assertTrue(dashboard_header.is_displayed())
            print("Username is NOT case-sensitive: Login successful with 'admin'")

        except Exception as e:
            self.fail(f"Login failed with lowercase username: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
