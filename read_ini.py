#coding=utf-8
import configparser
class ReadIni():
    def __init__(self,file_name=None,node=None):#默认就是空,node是配置文件节点值，即RegisterElement
        if file_name==None:
            file_name='E:\\汪蕾\\Python Selenium\\python\\LocalElement.ini'
        if node==None:
            self.node='RegisterElement'
        else:
            self.node=node
        self.cf=self.load_ini(file_name)
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf
        #cf.read('E:\\汪蕾\\Python Selenium\\python\\LocalElement.ini')

    def get_value(self,key):
        data=self.cf.get(self.node,key )
        return data
if __name__=='main()':
    read_ini=ReadIni()
    dd=read_ini.get_value('user_email')
    print(dd)