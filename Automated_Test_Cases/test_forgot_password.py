import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestForgotPassword(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)

    def test_forgot_password(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        forgot_password_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p"))
        )
        forgot_password_link.click()

        reset_header = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[text()='Reset Password']")
            )
        )

        self.assertTrue(reset_header.is_displayed())
        print("Successfully navigated to Reset Password page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
