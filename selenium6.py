'''
自动化测试框架：unittest
1.单元测试：是指对软件中最小可测试单元进行检查和验证，对于单元测试中单元的含义，一般来说，要根据实际
情况去判断其具体含义，如C语言中单元指一个函数
    function add(int a,int b){

    }
java里单元指一个类，图形化的软件中可以指一个窗口或一个菜单等，总的来说，单元就是人为规定的最小的测试
功能模板，单元测试是在软件开发过程中要进行的最低级别的测试活动，软件的独立单元将在与程序的其他部分相
隔离的情况下进行测试
2.unittest框架是python的单元测试框架，java->junit
3.unittest=TestCase+TestResult  执行+结果
4.单元测试unittest入门
    a.用import语句引入unittest模块
    b.测试的类都继承与TestCase类
    c.setUp()测试前的初始化工作，tearDown()测试后的清除工作（在每个测试方法运行时被调用）
    注意：1）所有类中方法的入参为self，定义方法的变量也要self.变量
        2）定义测试用例，以'test'开头命名的方法，方法的入参为self
        3）unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行他们
        4）自己写的Py文件不能用，用unittest.py命名，不然会找不到TestCase
        成功是输出，失败是F
5.
'''
#coding='utf-8'
from selenium import webdriver
import unittest
from time import sleep
# class UserTest(unittest.TestCase):
#     def setUp(self):
#         print('小D课堂开始')
#         self.name='xdclass'
#         self.age=28
#     def test_name(self):
#         self.assertEqual(self.name, 'xdclass', msg='匹配')
#     def test_issupper(self):
#         self.assertTrue('XDCLASS'.isupper(),msg='不是大写')
#         #self.assertFalse('XDCLASS'.isupper(),msg='是大写')
#     def test_age(self):
#         self.assertEqual(self.age,28)
#     def tearDown(self):
#         print('小D课堂结束')
# if __name__=='__main__':
#     unittest.main()

'''
测试套件TestSuite介绍
1.需求：1）利用unittest执行流程测试而非单元测试
    2）控制unittest的执行顺序
2.unittest.TestSuite()类来表示一个测试用例集
    1）用来确定测试用例的顺序，哪个先执行，哪个后执行
    2）如果一个class中有四个test开头的方法，则加载suite中时有四个测试用例
    3）由TestLoader加载TestCase到TestSuite
    4）verbosity参数可以控制执行结果的输出，0是简单报告，1是一般报告，2是详细报告，默认1，会在每个
    成功的用例前面有个'.'，每个失败用例前面有个F
3.TextTestRunner()文本测试用例运行器
4.run()方法是运行测试用例的套件，入参为suite测试套件


'''
# class XdclassTestCase(unittest.TestCase):
    # def setUp(self):
    #     self.age=32
    #     self.name='小D课堂'
    #     print('setup开始')
    # def tearDown(self):
    #     print('teardown method')
    #
    # def test_one(self):
    #     print('test one')
    #     self.assertEqual(self.name,'小D课堂',msg='名字不对')
    # def test_two(self):
    #     print('test two')
    #     self.assertFalse('xd'.isupper(),msg='不是大写')
    # def test_three(self):
    #     print('test three')
    #     self.assertEqual(self.age,32)

# if __name__=='__main__':
#     suite=unittest.TestSuite()
#     suite.addTest(XdclassTestCase('test_one'))#先找类再找类中对应的方法
#     suite.addTest(XdclassTestCase('test_two'))
#     runner=unittest.TextTestRunner()
#     runner.run(suite)
    #从上到下按照方法加入的顺序执行
'''
高级实战系列之测试套件TestSuite生成测试报告
HTMLTestRunner介绍

'''
import HTMLTestRunner
import time
class XdclassTestCase(unittest.TestCase):
    def setUp(self):
        self.age=32
        self.name='小D课堂'
        print('setup开始')
    def tearDown(self):
        print('teardown method')

    def test_one(self):
        u'测试测试'    #添加说明写入测试报告
        print('test one')
        self.assertEqual(self.name,'小D课堂',msg='名字不对')
    def test_two(self):
        print('test two')
        self.assertFalse('xd'.isupper(),msg='不是大写')
    def test_three(self):
        print('test three')
        self.assertEqual(self.age,32)

if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(XdclassTestCase('test_one'))#先找类再找类中对应的方法
    suite.addTest(XdclassTestCase('test_two'))
    #文件名加了当前时间为了每次生成不同的测试报告
    file=time.strftime('%Y-%n-%d %H_%M_%S',time.localtime())
    print(file)
    #创建测试报告，此时这个文件是空文件
    fp=open('C:\\Users\\Administrator\\Desktop\\report.html','wb')
    #以二进制格式打开一个文件，只用于写入，如果文件存在则覆盖，不存在则创建
    #stream定义一个测试报告写入的文件
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='小D课堂测试报告',description='测试用例执行情况')
    #runner=unittest.TextTestRunner()
    runner.run(suite)
    fp.close()
    #****ps：如果还是没有生成html报告，可以尝试alt+shift+f10+run运行代码
'''
unittest中测试报告优化
为每个测试用例添加说明，那么将会使报告更加易读懂，工作中汇报数据的技巧
'''