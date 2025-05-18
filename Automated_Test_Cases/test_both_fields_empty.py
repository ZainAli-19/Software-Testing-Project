import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestBothFieldsEmpty(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)

    def test_both_fields_empty(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        errors = driver.find_elements(By.XPATH, "//span[text()='Required']")
        self.assertEqual(len(errors), 2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()