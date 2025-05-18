import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPasswordMasking(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)

    def test_password_is_masked(self):
        driver = self.driver
        password_field = driver.find_element(By.NAME, "password")
        field_type = password_field.get_attribute("type")
        
        self.assertEqual(field_type, "password", "Password input is not masked (type != password)")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
