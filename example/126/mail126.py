from selenium import webdriver
import public
# #登陆
# def login():
#     driver.find_element_by_id("idInput").clear()
#     driver.find_element_by_id("idInput").send_keys("username")
#     driver.find_element_by_id("pwdInput").clear()
#     driver.find_element_by_id("pwdInput").send_keys("password")
#     driver.find_element_by_id("loginBtn").click()
# #退出
# def logout():
#     driver.find_element_by_link_text("退出").click()
#     driver.quit()

driver=webdriver.Chrome()
driver.get('https://www.126.com')
public.login(driver)#调用登陆模块
public.logout(driver)#调用退出模块