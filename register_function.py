'''
 1.以配置文件形式实现定位设计思想
 2.如何读取配置文件low代码:read_ini
 3. 重构封装读取配置文件方法:使用类class，read_ini.py
 4.设计封装定位元素类:find_element.py
 5.如何将整个注册流程脚本进行模块化实战讲解register_function.py
 6.注册失败进行截图处理:定位错误信息的元素然后截图
'''
#coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from find_element import *
class RegisterFunction():
    def __init__(self,url):
        self.driver=self.get_driver(url)
    #获取driver并且打开driver
    def get_driver(self,url):
        driver=webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver
    #输入用户信息
    def send_user_info(self,key,data):
        #定位用户信息，获取element,以便调用send_keys()方法
        self.get_user_element(key).send_keys(data)
    def get_user_element(self,key):
        findelement=FindElement(self.driver)
        userelement=findelement.get_element(key)
        return userelement

    # 获取随机数生成邮箱,用户名
    def get_range_user(self):
        user_info = ''.join(random.sample('123456789abcdefg', 5))
        return user_info

    # 获取验证码图片
    def get_code_image(self,file_name):  # 图片保存的地址
        self.driver.save_screenshot(file_name)
        code_ele = self.get_user_element('code_image')
        print(code_ele.location)  # 结果：{'x':123,'y':456}打印坐标，取出页面的图片
        left = code_ele.location['x']
        top = code_ele.location['y']
        right = code_ele.size['width'] + left
        height = code_ele.size['height'] + top
        image = Image.open(file_name)
        img = image.crop((left, top, right, height))  # 按照一定坐标裁剪，所以组成一个元组
        img.save('C:\\Users\\Administrator\\Desktop\\Sublime\\img1.png')

    # 获取图片后对图片进行解析获取具体的验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        return '调用第三方接口'  # 解析后最终返回一个text，例如：strck

    def run_main(self):
        user_name_info = self.get_range_user()  # 生成的随机数信息
        user_email = user_name_info + '@163.com'
        file_name = 'C:\\Users\\Administrator\\Desktop\\Sublime\\img1.png'
        code_text=self.code_online(file_name)
        self.send_user_info(self,'user_email',user_email)
        self.get_user_element('register-btn').click()
        time.sleep(5)
        self.driver.close()
if __name__=='main':
    register_function=RegisterFunction('http://www.5itest.cn/register')
    register_function.run_main()