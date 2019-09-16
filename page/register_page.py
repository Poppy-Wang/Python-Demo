'''
给handle层提供元素
page层需要通过定位方式找到页面的元素，所以创建base层，调用base层来查找元素，base文件夹放公共的东西
'''
#coding=utf-8
from base.find_element import FindElement
class RegisterPage():
    def __init__(self,driver):
        self.find_element=FindElement(driver)
    #获取邮箱元素
    def get_email_element(self):
        self.find_element.get_element('user_email')
    #获取用户名元素
    def get_name_element(self):
        self.find_element.get_element('user_name')

    #获取密码元素
    def get_password_element(self):
        self.find_element.get_element('password')
    #获取code元素
    def get_code_element(self):
        self.find_element.get_element('code_text')
    #点击事件
    def get_button_element(self):
        self.find_element.get_element('register-button')
    #获取邮箱错误元素
    def get_email_error_element(self):
        self.find_element.get_element('user_email_error')
    def get_name_error_element(self):
        self.find_element.get_element('user_name_error')
    def get_password_error(self):
        self.find_element.get_element('password_error')
    def get_code_error(self):
        self.find_element.get_element('code_text_error')

