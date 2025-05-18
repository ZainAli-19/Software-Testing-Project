import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestBackButtonAfterLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)

    def test_browser_back_button_after_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        wait.until(EC.url_contains("dashboard"))
        self.assertIn("dashboard", driver.current_url)
        driver.back()
        WebDriverWait(driver, 5).until(lambda d: True)  

        current_url = driver.current_url
        if "dashboard" in current_url:
            print("Back button did not allow access to login: secure behavior.")
        else:
            login_button = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))
            )
            self.assertTrue(login_button.is_displayed())
            print("Redirected back to login page after back button: secure behavior.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
