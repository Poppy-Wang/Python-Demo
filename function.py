#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
# title=driver.title
# url=driver.current_url
# print(title)
# print(url)
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
# driver.find_element_by_id('kw').send_keys(Keys.SPACE)
# driver.find_element_by_id('kw').send_keys('教程')
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
# driver.find_element_by_id('su').send_keys(Keys.ENTER)
element=WebDriverWait(driver,5,0.5).until(
    EC.presence_of_element_located((By.ID,"kw"))
    #lambda driver : input.is_displayed()
)
element.send_keys('selenium')



