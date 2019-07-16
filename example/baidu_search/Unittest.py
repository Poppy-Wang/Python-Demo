import unittest
from selenium import webdriver
class baiduTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(50)
        self.base_url='https://www.baidu.com'
    def test_Baidu(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').send_keys('selenium')
        driver.find_element_by_id('su').click()
    def test_youdao(self):
        driver=self.driver
        driver.get('https://www.youdao.com')
    def tearDown(self):
        self.driver.quit()
if __name__=='main':
    unittest.main()#整个测试过程集成在 unitest.main()模块中，其默认执行以 test 开头的方法
