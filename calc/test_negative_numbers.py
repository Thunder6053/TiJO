import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestNegativeNumbers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://tgadek.bitbucket.io/app/calc/dev/index.html')

    def test_negative_input(self):
        self.driver.find_element(By.ID, "number1").send_keys("-2")
        self.driver.find_element(By.ID, "number2").send_keys("3")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result,"0")

    def tearDown(self):
        self.driver.quit()