#coding=utf-8
from selenium import webdriver
import time
import os
driver=webdriver.Chrome()
#C:\Users\lei.wang9\Desktop\wang\PDF
path='C:\\Users\\lei.wang9\\Desktop\\wang\\PDF\\frame.html'
file_path=os.path.abspath(path)
driver.get(file_path)
driver.switch_to.frame('if')#默认可以直接取表单的 id 或 name 属性进行切换,如果 iframe 没有可用的 id 和 name,
                            #先通过方法定位到 iframe,再将定位对象传给 switch_to_frame()方法
#下面就可以正常的操作元素了
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)