#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract
driver=webdriver.Chrome()
driver.get('http://www.5itest.cn/register')
driver.maximize_window()
time.sleep(5)
print(EC.title_contains('注册'))#判断页面是否有注册
#xpath定位的时候如果双引号之间还有引号，要改成单引号

#locator=(By.ID,'register_email')
#WebDriverWait(driver,10).until(EC.visibility_of_element_located(ele))报错根据源码可以知道传入的参数不对
#WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))
#判断找到的元素是否可见，没有找到则报错，找到继续下一步
#driver.close()

#输入注册用户名字获取注册信息的属性值
# ele=driver.find_element_by_id('register_email')
# atr=ele.get_attribute('placeholder')
# print(atr)
# ele.send_keys('15829765307@163.com')
# print(ele.get_attribute('value'))

#如何生成用户名
# for i in range(4):
#     phone =''.join(random.sample('123456789', 5))+'@163.com'
#     print(phone)

'''
如何解决验证码思路
1.设置一个万能的验证码
2.通过cookie绕过验证码
3.识别验证码图片进行解析
'''
driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\Sublime\\img.png')
code_ele=driver.find_element_by_id('getcode_num')
print(code_ele.location)#结果：{'x':123,'y':456}打印坐标，取出页面的图片
left=code_ele.location['x']
top=code_ele.location['y']
right=code_ele.size['width']+left
height=code_ele.size['height']+top
image=Image.open('C:\\Users\\Administrator\\Desktop\\Sublime\\img.png')
img=image.crop((left,top,right,height))#按照一定坐标裁剪，所以组成一个元组
img.save('C:\\Users\\Administrator\\Desktop\\Sublime\\img1.png')
#使用pytesseract识别解析图片遇到的问题，针对规则性的验证码有效，不规则的不适合
# mm=Image.open('C:\\Users\\Administrator\\Desktop\\Sublime\\img1.png')
# text=pytesseract.image_to_string(mm)
# print(text)
#ShowapiRequest解决图片验证码识别，调用第三方公司api
