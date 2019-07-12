from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.126.com')

class Account:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def login(self):
        driver.find_element_by_id("idInput").clear()
        driver.find_element_by_id("idInput").send_keys("username")
        driver.find_element_by_id("pwdInput").clear()
        driver.find_element_by_id("pwdInput").send_keys("password")
        driver.find_element_by_id("loginBtn").click()
Admin=Account('yoyo','123')
customer=Account('yy','456')
Admin.login()
customer.login()

