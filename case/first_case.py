'''
po模型设计思想
case层用于最后进行测试的地方。，调用业务层的方法
'''
#coding=utf-8
from business.register_business import RegisterBusiness
class FirstCase():
    def __init__(self):
        self.registerbusiness=RegisterBusiness()
    def test_login_email_error(self):
        self.registerbusiness.login('121','111','12121','2112121')
        pass
    def test_login_username_error(self):
        self.registerbusiness.login('121', '111')
        pass
    def test_login_code_error(self):
        self.registerbusiness.login('121', '111')
        pass
    def test_login_password_error(self):
        self.registerbusiness.login('111','3253')
    def test_login_success(self):
        self.registerbusiness.login('121', '111')
        pass