#登陆
def login(driver):
    driver.find_element_by_id("idInput").clear()
    driver.find_element_by_id("idInput").send_keys("username")
    driver.find_element_by_id("pwdInput").clear()
    driver.find_element_by_id("pwdInput").send_keys("password")
    driver.find_element_by_id("loginBtn").click()
#退出
def logout(driver):
    driver.find_element_by_link_text("退出").click()
    driver.quit()