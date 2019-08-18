'''
自动化测试selenium和unittest整合项目实战
1.小D课堂官网项目实战需求说明
简介：讲解小D课堂官方自动化测试需求场景，和项目基础框架搭建
1）自动化测试里面的测试用例设计的一些方法
    解耦，可以独立运行，需要灵活切换
    设计思路：脚本功能分析（分步骤）和模块化分层（拆分为多模块）
    project
        login_order.py登录下单测试用例
        category.py菜单分类测试用例
        all_test.py主入口

'''
'''
自动化测试实战之下单自动化测试
使用selenium+unittest自动化测试用例编写

'''
import unittest
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
# class LoginOrderTestCase(unittest.TestCase):
#     def setUp(self):
#         print('测试开始')
#         self.driver=webdriver.Chrome()
#         self.driver.implicitly_wait(20)
#         self.driver.maximize_window()
#         self.base_url='https://www.xdclass.net'
#         self.driver.get(self.base_url)
#     # def tearDown(self):
#     #     print('测试结束')
#     #     pass
#     def test_login_order(self):
#         #登录测试用例
#         driver=self.driver
#         #登陆框
#         login_ele=driver.find_element_by_css_selector('#app > div > div.header > div > div.r_userinfo.f_r > div.login > span:nth-child(2)')
#         ActionChains(driver).click(login_ele).perform()
#         sleep(2)
#         #查找用户名输入框，输入账号
#         driver.find_element_by_css_selector('#app > div > div.header > div.main > div.login > div > div.mobienum > input[type=text]').clear()
#         driver.find_element_by_css_selector('#app > div > div.header > div.main > div.login > div > div.mobienum > input[type=text]').send_keys('15829765307')
#         #查找密码输入框，输入密码
#         driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[2]/input').clear()
#         driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[2]/input').send_keys('wangyiwei1993')
#         #点击登录button
#         login_btn_ele=driver.find_element_by_class_name('btn').click()
#         #判断用户是否登录成功,鼠标hover到用户登录头像
#         user_info_ele=driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/div[3]/img')
#         ActionChains(driver).move_to_element(user_info_ele).perform()
#         # 获取用户名
#         user_name=driver.find_element_by_class_name('username')
#         print('测试结果')
#         print(user_name.text)
#         #寻找下单元素
#         driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/a[1]/div/img').click()
#         sleep(3)
#         #切换到新窗口
#         windows = driver.window_handles
#         driver.switch_to.window(windows[1])
#         #buy_btn=driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[2]/div[1]/div[1]/a')
#         buy_btn=driver.find_element_by_css_selector('#app > div > div.details_container.clearfix > div.body.w > div.r_container.f_r > div.gostudy > div.buy_tolearn > a')
#         buy_btn.click()
#         print('进入下单页面')
# if __name__=='main':
#     unittest.main()

'''
分类列表整合unittest自动化测试
使用selenium+unittest菜单弹框测试用例编写

'''
# class Category(unittest.TestCase):
#     def setUp(self):
#         print('测试开始')
#         self.driver=webdriver.Chrome()
#         self.driver.implicitly_wait(20)
#         self.driver.maximize_window()
#         self.base_url='https://www.xdclass.net'
#         self.driver.get(self.base_url)
#     # def tearDown(self):
#     #     print('测试结束')
#     #     self.driver.quit()
#     def test_menu(self):
#         u'弹出菜单测试用例'
#         driver=self.driver
#         sleep(2)
#         #定位到主菜单：后端.鼠标hover上去
#         menu_ele=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/ul/li[1]')
#         ActionChains(driver).move_to_element(menu_ele).perform()
#         #定位子菜单java
#         sub_menu_ele=driver.find_element_by_link_text('java').click()
# if __name__=='main':
#     unittest.main()
'''
发送测试报告邮件
讲解发送邮件的基础知识
1.邮件发送的基本过程和概念
邮件服务器：类似于现实生活中的邮局，主要负责接收用户投过来的邮件，并把邮件投递到邮件接受者的电子邮箱中
电子邮箱：用户在邮件服务器上申请的一个账户
from：发件人
to:收件人
subject:主题
2.邮件传输协议：
SMTP协议：简单邮件传输协议，它定义了邮件客户端软件和SMTP邮件服务器之间，
以及两台SMTP两台邮件服务器之间的通信规则
POP3协议：邮局协议，它定义了邮件客户端软件和POP3邮件服务器的通信规则
IMAP协议：internet消息访问协议，它是对POP3协议的一种扩展，也是定义了邮件客户端软件和IMAP邮件
服务器的通信规则

'''
'''
使用python发送邮件实战

'''
import smtplib
import os
import datetime
from email.mime.text import MIMEText
from email.header import Header
#收件人发件人
sender='15829765307.163.com'
reciver='850580407@qq.com'
#850580407@qq.com   15829765307.163.com
#不用密码发送，而是用授权码发送
auth_code='wanglei2016'
#password='wanglei2016@'
subject='自动化测试报告'
msg=MIMEText('<html> <h2>欢迎来到小D课堂</h2> </html>',_subtype='html',_charset='utf-8')
msg['Subject']=subject
msg['from']=sender
msg['to']=reciver

#mail_host='smtp.163.com'
#smtp=smtplib.SMTP_SSL(mail_host,'465')
smtp=smtplib.SMTP('smtp.163.com')
#smtp.connect('smtp.163.com')
smtp.login(sender,auth_code)
smtp.sendmail(sender,reciver,msg.as_string())
smtp.quit()


