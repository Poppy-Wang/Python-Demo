import unittest
from selenium import webdriver
class Test_baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url1='https://www.baidu.com'
    def test_Baidu(self):
        driver=self.driver
        driver.get(self.url1)
        driver.find_element_by_id('kw').send_keys('selenium')
        driver.find_element_by_id('su').click()
    def tearDown(self):
        pass
if __name__=='main':
    unittest.main()