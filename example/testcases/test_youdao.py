import unittest
from selenium import webdriver
class Test_youdao(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url2='https://www.youdao.com'
    def test_youdao(self):
        driver=self.driver
        driver.get(self.url2)
    def tearDown(self):
        pass
if __name__=='main':
    unittest.main()