#coding=utf-8
from selenium import webdriver
import time
import os
import logging
# driver=webdriver.Chrome()
# #C:\Users\lei.wang9\Desktop\wang\PDF
# path='C:\\Users\\lei.wang9\\Desktop\\wang\\PDF\\frame.html'
# file_path=os.path.abspath(path)
# driver.get(file_path)
# driver.switch_to.frame('if')#默认可以直接取表单的 id 或 name 属性进行切换,如果 iframe 没有可用的 id 和 name,
#                             #先通过方法定位到 iframe,再将定位对象传给 switch_to_frame()方法
# #下面就可以正常的操作元素了
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# time.sleep(3)
#上传文件
driver=webdriver.Chrome()
# #C:\Users\lei.wang9\Desktop\wang\PDF
# #打开上传文件的页面
# path='C:\\Users\\lei.wang9\\Desktop\\wang\\PDF\\uploadfile.html'
# file_path=os.path.abspath(path)
# driver.get(file_path)
# #定位到上传button，通过本地文件的路径上传文件
# #通过 send_keys()方法向其输入一个文件地址来实现上传
# driver.find_element_by_name("file").send_keys('C:\\Users\\lei.wang9\\Desktop\\wang\\PDF\\frame.html')

#获取浏览器cookie
driver.get('http://www.youdao.com')
## 获得 cookie 信息
#cookie=driver.get_cookies()
#打印cookie信息
#print(cookie)
#截图
logging.basicConfig(level=logging.DEBUG)
driver.get_screenshot_as_file('C:\\Users\\lei.wang9\\Desktop\\wang\\PDF\\picture.png')
driver.add_cookie({'name':'111','value':'22222'})
for cookie in driver.get_cookies():
    print(cookie)


