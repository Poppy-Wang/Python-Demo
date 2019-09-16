'''
定位元素
'''
#coding=utf-8
from read_ini import ReadIni
class FindElement():
    def __init__(self,driver):
        self.driver=driver
    def get_element(self,key):
        read_ini=ReadIni()
        data=read_ini.get_value(key)
        by=data.split('>')[0]
        value=data.split('>')[1]
        try:
            if by=='id':
                return self.driver.find_element_by_id(value)
            elif by=='className':
                return self.driver.find_element_by_class_name(value)
        except:
            return None