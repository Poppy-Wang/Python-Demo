'''
selenium 之模拟事件处理
简介：使用selenium里的ActionChains模拟用户的行为
需求：需要模拟鼠标操作才能进行的情况，比如单击，双击，点击鼠标右键，拖曳
解决：selenium提供了一个类来处理这类事件
     selenium.webdriver.common.action_chains.ActionChains(driver)
     脚本： import selenium.webdriver.common.action_chains.ActionChains(driver)
执行原理：
    调用ActionChains的方法时不会立即执行，会将所有的操作按顺序存放在一个队列里，当调用perform
    方法时，队列中的事件会一次执行
    支持链式写法或分步写法
    ActionChains(driver).click(ele).perform()
常用鼠标和键盘方法列表：
perform()执行链中的所有动作
click(on_element=None)单击鼠标左键
context_click(on_element=None)点击鼠标右键
double_click(on_element=None)双击鼠标左键
move_to—_element(on_element=None)鼠标移到某个元素
ele.send_keys(keys_to_send)发送某个次到当前焦点的元素
鼠标事件实战之hover菜单栏弹出
1.引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
2.move_to_element(to_element)鼠标移动到某个元素
#对定位到的元素执行鼠标移动到上面的操作
ActionChains(driver).move_to_element(to_element).perform()
----见例1
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#例1
# driver=webdriver.Chrome()
# driver.get('https://www.xdclass.net')
# print(driver.title)
# sleep(5)
# #定位鼠标想要移动的元素
# menue_ele=driver.find_element_by_css_selector('.list_item > li:nth-child(1)')
# sleep(5)
# #定位元素后鼠标执行hover操作
# ActionChains(driver).move_to_element(menue_ele).perform()
# #选中子菜单
# sub_menue=driver.find_element_by_css_selector('.base > div:nth-child(3) > a:nth-child(1)')
# sleep(2)
# sub_menue.click()

'''
多知识点综合实战之模拟用户登录
1.多知识点实战
2.查找登陆框——输入用户名和密码——触发登录——判断登录是否成功——打印结果
---见例2
'''
#例2登录实战
# driver=webdriver.Chrome()
# driver.get('https://www.xdclass.net')
# print(driver.title)
# sleep(3)
# #寻找登录元素
# login_button=driver.find_element_by_css_selector('.login > span:nth-child(2)')
# ActionChains(driver).click(login_button).perform()
# #点击取消自动登录功能
# driver.find_element_by_xpath('.login_btn > span:nth-child(1) > input:nth-child(1)').click()
# #寻找输入框，输入用户名和密码
# #输入用户名
# username=driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div/div[1]/input')
# username.clear()
# username.send_keys('15829765307')
# #输入密码
# password=driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div/div[2]/input')
# password.clear()
# password.send_keys('wangyiwei1993')
# #需找登录button点击
# login=driver.find_element_by_class_name('btn')
# ActionChains(driver).click(login).perform()
# #判断是否登录成功，鼠标移到上面判断弹窗字符
# user_info=driver.find_element_by_css_selector('#app > div > div.header > div > div.r_userinfo.f_r > div.avatar.f_r > img')
# sleep(3)
# ActionChains(driver).move_to_element(user_info).perform()
# #获取用户名的元素
# login_name=driver.find_element_by_class_name('username')
# #打印文本值
# print(login_name.text)
# if login_name=='小小夏':
#     print('用户名正确')
# else:
#     print('用户不正确')

'''
自动化实战之网页等待时间
1.为什么需要等待时间——>等待系统稳定
    网页需要加载对应的资源文件，页面渲染，窗口处理等等
2.自动化测试常用的等待时间
    强制等待：
    from time import sleep
    sleep(3)强制等待3秒再执行下一步，缺点是不管资源是不是完成，都必须等待
    隐性等待：
    driver.implicitly_wait()隐性等待，最长等待10秒
    设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后
    执行下一步，弊端就是程序会一直等待整个页面加载完成，到浏览器标签栏那个加载圈不再转
    注意：对driver起作用，所以只要设置一次即可，没有必要到处设置
    显性等待：
    WebDriverWaite需要配合
    until和until_not，程序每隔N秒检查一次，如果成功则执行下一步，否则继续等待，直到超过设置的最长时间
    from selenium.webdriver.support.wait import WebDriverWait
    语法：
    WebDriverWait.(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
    timeout：最长超时时间
    poll_frequency:检查时间
    ignored_exceptions=None：是否忽略异常
    
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
----见例3、4
'''
#例3
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com')
# #sleep(3)
# driver.implicitly_wait(5)
# print(driver.title)
#driver.get('https://www.xdclass.net')

#例4
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
try:
    ele=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'kw')))
    ele.send_keys('python').click()
    print(driver.title)
except:
    print('资源未找到')
finally:
    print('不管有没有找到，都打印，用于资源清理')