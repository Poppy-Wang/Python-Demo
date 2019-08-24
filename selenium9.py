'''
注册流程梳理及代码封装

'''
#coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image

driver=webdriver.Chrome()
#浏览器初始化
def driver_init():#driver初始化封装
    driver.get('http://www.5itest.cn/register')
    driver.maximize_window()
    time.sleep(5)
#获取element信息
def get_element(id):#每次都需要去查找输入框，所以封装成方法后直接去找对于的定位方式即可
    element=driver.find_element_by_id(id)
    return element
#获取随机数生成邮箱,用户名
def get_range_user():
    user_info=''.join(random.sample('123456789abcdefg',5))
    return user_info
#获取验证码图片
def get_code_image(file_name):#图片保存的地址
    driver.save_screenshot(file_name)
    code_ele = driver.find_element_by_id('getcode_num')
    print(code_ele.location)  # 结果：{'x':123,'y':456}打印坐标，取出页面的图片
    left = code_ele.location['x']
    top = code_ele.location['y']
    right = code_ele.size['width'] + left
    height = code_ele.size['height'] + top
    image = Image.open(file_name)
    img = image.crop((left, top, right, height))  # 按照一定坐标裁剪，所以组成一个元组
    img.save('C:\\Users\\Administrator\\Desktop\\Sublime\\img1.png')
#获取图片后对图片进行解析获取具体的验证码
def code_online(file_name):
    return '调用第三方接口'#解析后最终返回一个text，例如：strck
#运行主程序
def run_main():
    driver_init()
    user_name_info = get_range_user()#生成的随机数信息
    user_email=user_name_info+'@163.com'
    file_name='C:\\Users\\Administrator\\Desktop\\Sublime\\img1.png'
    get_element('register_email').send_keys(user_email)
    get_element('register_nickname').send_keys(user_name_info)
    get_element('register_password').send_keys('111111')
    get_code_image(file_name)
    text=code_online(file_name)
    get_element('captcha_code').send_keys(text)
    get_element('register-btn').click()
    driver.close()
run_main()
