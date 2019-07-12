from selenium import webdriver
file_info = open('info.txt','r')
values = file_info.readlines()
file_info.close()
for serch in values:
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys(serch)
    driver.find_element_by_id('su').click()
    driver.quit()
#首先通过 open()方法以读（‘r’）的方式打开当前目录下的 info.txt 文件，通过 readlines()获取
# 文件中所有行的数据，并赋值给变量 values。通过 close()关闭文件。
# 接下来的步骤就是循环的执行百度搜索的脚本，每一次取 vlaues 中的一行数据做为“搜索关键字”
# 传递给百度输入框。通过这个例子更充分的体现有数据驱动的概念