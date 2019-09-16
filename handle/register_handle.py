#coding=utf-8
'''
操作层，用于输入的地方
输入数据之后要进行操作，即业务层(case和handle层之间缺少business层，handle层在输入数据后要对数据
进行操作，即校检数据)
输入数据之前要对页面进行操作，即找到该元素
handle层调用page层,page层即页面
'''
from page.register_page import RegisterPage
class RegisterHandle():
    def __init__(self):
        self.register_P=RegisterPage()
    #输入邮箱
    def send_user_email(self,email):
        self.register_P.get_email_element().send_keys(email)
        pass
    #输入用户名
    def send_user_name(self,name):
        self.register_P.get_name_element().send_keys(name)
        pass
    #输入密码
    def send_user_password(self,password):
        self.register_P.get_name_element().send_keys(password)
        pass
    #输入验证码
    def send_user_code(self,code):
        self.register_P.get_name_element().send_keys(code)
        pass
    #获取文字信息，指用户输入有误时的错误提示
    def get_user_text(self,info,user_info):
        if info=='user_email_error':
            self.register_P.get_email_error_element().get_attribute('value')
        pass
    #点击注册按钮
    def click_register_button(self):
        pass