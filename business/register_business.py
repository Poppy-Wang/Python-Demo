'''
注册页面的操作
业务层设计
'''
#coding=utf-8
from handle.register_handle import RegisterHandle
class RegisterBusiness():
    #实例化
    def __init__(self,driver):
        self.register_H=RegisterHandle(driver)
    #执行操作
    def login(self,email,name,password,code):
        #需要校检输入的数据是否符合要求
        self.register_H.send_user_email(email)
        self.register_H.send_user_name(name)
        self.register_H.send_user_password(password)
        self.register_H.send_user_code(code)
        self.register_H.click_register_button()
        if self.register.get_user_text('user_email_error','请输入有效的电子邮箱地址'):
            print('邮箱检验成功')
        elif self.register_H.get_user_text('user_name_error','用户名应该长度大于4'):
            print('用户名检验成功')

