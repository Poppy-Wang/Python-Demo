'''
一、selenium基础实战之定位网页元素技巧
find_element_by_id/find_element_by_name/find_element_by_class_name
1.打开浏览器
 broswer=webdriver.Chrome()
2.打开网页
broswer.get('https://www.baidu.com')
使用python判断是否正确
broswer.title或者broswer.current_url
3.定位元素的八种方法(一定要唯一)
1)id: find_element_by_id()采用id属性定位
2)name:find_element_by_name()定位方式和id定位相似，id,name和class一般在网页都至少会有其中的一种
3)class name:find_element_by_class_name()定位方式和id相似，id/name和class一般在网页都至少会有其中的一种
4)tag name:find_element_by_tag_name()通过标签名去ID年改为，用的少，如find_element_by_tag_name('div')
5)link text:find_element_by_link_text()超链接内容定位，元素内容
如<a herf='#'>xxx</a>则find_element_by_link_text('xxx')
from time import sleep
sleep(5)
6）partial link text:find_element_by_partial_link_text()超链接内容，模糊匹配，和上面类似
7)css selector:find_element_by_css_selector()根据css属性定位，一般class用.标记,id是用#标记，定位方式也会比xpath快
技巧：通过firebug的拷贝css路径
8)xpath定位：语法：参考W3c教程
        ‘//’是全部的意思，‘、’相邻的意思，*所有元素，'..'是元素的父元素,'.'当前节点
xpath：find_element_by_xpath()xpath是xml路径，通过元素的路径来完成元素的查找，可以在firefox里copy xpath

选择器注意问题：如果元素定位报错——根据定位取不到；多个元素根据下标超出范围，没有0从1开始
解决办法：采取其他方式定位
4.定位到元素后的方法
clear()清空
send_keys()输入
back()后退
maximize_window()最大化窗口
click()点击事件，点击按钮，超链接
'''
#coding=utf-8
from selenium import webdriver
from time import sleep
#例1   id定位
#拿到driver
# driver=webdriver.Chrome()
# #跳转网页
# driver.get("https://www.baidu.com")
# #打印title
# print(driver.title)
# #选中输入框并输入关键词
# driver.find_element_by_id('kw').send_keys('小D课堂')
# #点击百度一下按钮
# driver.find_element_by_id('su').click()

# #例2   name定位
# #拿到driver
# driver=webdriver.Chrome()
# #跳转网页
# driver.get("https://www.baidu.com")
# #打印title
# print(driver.title)
# #选中输入框并输入关键词
# driver.find_element_by_name('wd').send_keys('springboot小D课堂')
# #点击百度一下按钮
# driver.find_element_by_id('su').click()

# #例3  class name定位
# #拿到driver
# driver=webdriver.Chrome()
# #跳转网页
# driver.get("https://www.baidu.com")
# #打印title
# print(driver.title)
# #选中输入框并输入关键词
# driver.find_element_by_class_name('s_ipt').send_keys('springboot小D课堂')
# #点击百度一下按钮
# driver.find_element_by_id('su').click()


#例4  link text定位
# driver=webdriver.Chrome()
# driver.get('https://www.xdclass.net')
# sleep(5)
# print(driver.title)
# driver.find_element_by_link_text('工具').click()

#例5 css 定位
# driver=webdriver.Chrome()
# driver.get('https://www.xdclass.net')
# sleep(5)
# print(driver.title)
# driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[2]/ul/li[2]').click()
# driver.find_element_by_css_selector('.courselist > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > img:nth-child(2)').click()


# 例6  xpath
driver=webdriver.Chrome()
driver.get('https://www.xdclass.net')
sleep(5)
print(driver.title)
driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/a[1]/div/img').click()









