'''
自动化测试进阶实战篇
1.自动化测试实战进阶之网页单选性别资料实战
    简介：讲解使用selenium修改input输入框和单选框
'''
from selenium import webdriver
from time import sleep

# driver=webdriver.Chrome()
# driver.get('C:\\Users\\Administrator\\Desktop\\Sublime\\HTML\\index.html')
# print(driver.title)
# print('默认选中男，2秒后选中女')
# sleep(2)
# driver.find_element_by_id('femal').click()

'''
自动化测试之页面常见弹窗处理
1.selenium处理页面弹窗，alert和confirm
    弹窗常用方法(需要先切换窗口:switch_to_alert)：
        accept()和dismiss()
'''
# driver=webdriver.Chrome()
# driver.get('C:\\Users\\Administrator\\Desktop\\Sublime\\HTML\\index1.html')
# driver.implicitly_wait(2)
# #点击alert按钮
# driver.find_element_by_id('alert').click()
# sleep(2)
# #切换到alert弹窗窗口
# btn1=driver.switch_to.alert
# btn1.accept()
# #点击confirm按钮
# driver.find_element_by_id('confirm').click()
# sleep(3)
# #切换到confirm弹窗窗口点击取消
# btn2=driver.switch_to.alert
# btn2.dismiss()

'''
自动化测试之常见验证码解决方案
1.破解验证码
    OCR识别：tesseract-ocr(python插件)
    AI机器学习
2.绕过验证码
    让开发人员临时关闭验证码（安全性需要保密，一般在开发测试环境使用）
    提供一个万能的验证码（安全性需要保密，一般在开发测试环境使用）
    使用cookie（登录主要是为了拿cookie，获取登录凭证）

自动化测试实战之cookie操作

'''
driver=webdriver.Chrome()
driver.get('https://www.xdclass.net')
driver.maximize_window()
print(driver.title)
sleep(3)
# driver.add_cookie({'name':'token','value':'xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMTkuanBlZyIsImlkIjoxMTcwOSwibmFtZSI6IuWwj-Wwj-WkjyIsImlhdCI6MTU2NDQ5Mzc2NiwiZXhwIjoxNTY1MDk4NTY2fQ.OyFvEwU5c8XxMcHqTEGcWxUhj5w5FM7LJIcURIV0mwk'})
# video_ele=driver.find_element_by_css_selector('#app > div > div.hot > div > div.content > a:nth-child(1) > div > img')
# video_ele.click()
# sleep(2)
# buy=driver.find_element_by_css_selector('#app > div > div.details_container.clearfix > div.body.w > div.r_container.f_r > div.gostudy > div.buy_tolearn > a')
# buy.click()

'''
自动化测试截图
使用webdriver自动截图
driver.get_screenshot_as_file()括号里写路径
'''
driver.get_screenshot_as_file('C:\\Users\\Administrator\\Desktop\\Sublime\\xd.png')










