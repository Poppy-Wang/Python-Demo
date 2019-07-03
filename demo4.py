import math
'''
python函数：通常，函数可以接收零个或多个参数，也可以返回零个或多个值
1.在使用函数之前必须先定义函数，定义函数的语法格式如下：
def 函数名(形参列表):
    //由零条到多条可执行语句组成的函数
    [return [返回值]]
Python 声明函数必须使用 def 关键字，对函数语法格式的详细说明如下：
a.函数名：从语法角度来看，函数名只要是一个合法的标识符即可；从程序的可读性角度来看，函数名应该由一个或多个有意义的单词连缀而成，
每个单词的字母全部小写，单词与单词之间使用下画线分隔。
b.形参列表：用于定义该函数可以接收的参数。形参列表由多个形参名组成，多个形参名之间以英文逗号（,）隔开。一旦在定义函数时指定了形参列表，
调用该函数时就必须传入到应的参数值，也就是说，谁调用函数谁负责为形参赋值。
2.在函数体中多条可执行语句之间有严格的执行顺序，排在函数体前面的语句总是先执行，排在函数体后面的语句总是后执行
3.当程序调用一个函数时，既可以把调用函数的返回值赋值给指定变量，也可以将函数的返回值传给另一个函数，作为另一个函数的参数。
4.return 语句可以显式地返回一个值，return 语句返回的值既可是有值的变量，也可是一个表达式
5.程序既可通过 help() 函数查看函数的说明文档，也可通过函数的 __doc__ 属性访问函数的说明文档。下面程序示范了为函数编写说明文档：
'''
#例1
# def my_max(x,y):#定义一个函数声明2个形参
#     #定义一个变量z用于接收x,y中较大的值
#     if x>y:
#         z=x
#     else:
#         z=y
#     return z#返回变量z的值
# def say_hi(name):#定义一个函数声明一个形参
#     print("==正在执行say_hi函数==")
#     return name+"，你好"
# a=6
# b=9
# result=my_max(a,b)
# print('result:',result)
# print(say_hi('孙悟空'))
# help(my_max)
# print(my_max.__doc__)

'''
python函数返回多个值
1.如果程序需要有多个返回值，则既可将多个值包装成列表之后返回，也可直接返回多个值。如果 Python 函数直接返回多个值，
Python 会自动将多个返回值封装成元组;也可使用 Python 提供的序列解包功能，直接使用多个变量接收函数返回的多个值。
'''
#例2
# def sum_and_avg(list):
#     sum=0
#     count=0
#     for e in list:
#         #如果元素e是数值
#         if isinstance(e,int) or isinstance(e,float):
#             count+=1
#             sum+=e
#     return sum,round(sum/count,2)
# my_list = [20, 15, 2.8, 'a', 35, 5.9, -1.8]
# # 获取sum_and_avg函数返回的多个值，多个返回值被封装成元组
# tp = sum_and_avg(my_list)
# print(tp)
# s,avg=sum_and_avg(my_list)#使用多个变量接收返回的多个值
# print(s)
# print(avg)
'''
python函数递归：在一个函数体内调用它自身，被称为函数递归
在定义递归函数时有一条最重要的规定： 递归一定要向已知方向进行
'''
#例3己知有一个数列：f(0) = 1，f(1) = 4，f(n + 2) = 2*f(n+ 1) +f(n)，其中 n 是大于 0 的整数，求 f(10) 的值
# def fn(n):
#     if n==0:
#         return 1
#     elif n==1:
#         return 4
#     else:
#         # 函数中调用它自身，就是函数递归
#         return 2 * fn(n - 1) + fn(n - 2)
# #输出fn(10)的值
# print("fn(10)的值：",fn(10))
'''
函数参数
1.关键字参数：
    a.按照形参位置传入的参数被称为位置参数。如果使用位置参数的方式来传入参数值，则必须严格按照走义函数时
指定的顺序来传入参数值；如果根据参数名来传入参数值，则无须遵守定义形参的顺序，这种方式被称为关键字（keyword）参数。
    b.如果希望在调用函数时混合使用关键字参数和位置参数，则关键字参数必须位于位置参数之后。换句话说，在关键字参数之后的只能是
关键字参数。例如如下代码是错误的:
print(girth(width = 3.5, 4.8))
2.默认参数：
    a.在某些情况下，程序需要在定义函数时为一个或多个形参指定默认值，这样在调用函数时就可以省略为该形参传入参数值，
    而是直接使用该形参的默认值。
    b.为形参指定默认值的语法格式如下：
        形参名 = 默认值
    形参的默认值紧跟在形参之后，中间以英文“=”隔开
    c.如果只传入一个位置参数，由于该参数位于第一位，系统会将该参数值传给 name 参数。
    d.由于 Python 要求在调用函数时关键字参数必须位于位置参数的后面，因此在定义函数时指定了默认值的参数（关键字参数）
    必须在没有默认值的参数之后
3.可变参数：
    a.很多编程语言都允许定义个数可变的参数，这样可以在调用函数时传入任意多个参数。Python 当然也不例外，Python 允许在
    形参前面添加一个星号（*），这样就意味着该参数可接收多个参数值，多个参数值被当成元组传入,参数收集的本质就是元组
    b.Python 允许个数可变的形参可以处于形参列表的任意位置（不要求是形参列表的最后一个参数），但 Python 要求一个函数
    最多只能带一个支持“普通”参数收集的形参。
    c.Python 还可以收集关键字参数，此时 Python 会将这种关键字参数收集成字典。为了让 Python 能收集关键字参数，
    需要在参数前面添加两个星号。
    
    
'''
#例4
# def girth(width,height):
#     print('width:',width)
#     print('height:',height)
#     return 2*(width+height)
# #调用传统函数的方式，根据位置参数传参
# print(girth(3.5,4.6))
# #根据关键字参数传参,使用关键字 参数时可以交换位置
# print(girth(height=4.6,width=3.5))
# print(girth(width=3.5,height=4.6))
# #部分使用关键字参数，部分使用位置参数
# print(girth(3.5,height=4.6))
#例5
# 为两个参数指定默认值
# def say_hi(name='kk',message='欢迎到来'):
#     print(name,'你好')
#     print('消息是：',message)
# # 全部使用默认参数
# say_hi()
# #只有message参数使用默认值
# say_hi('白骨精')
# # 两个参数都不使用默认值
# say_hi("白骨精", "欢迎学习Python")
# # 只有name参数使用默认值
# say_hi(message="欢迎学习Python")
#例6
# 定义一个打印三角形的函数，有默认值的参数必须放在后面
# def printTriangle(char, height = 5) :
#     for i in range(1, height + 1) :
#         # 先打印一排空格
#         for j in range(height - i) :
#             print(' ', end = '')
#         # 再打印一排特殊字符
#         for j in range(2 * i - 1) :
#             print(char, end = '')
#         print()
# printTriangle('@', 6)
# printTriangle('#', height=7)
# printTriangle(char = '*')

# a=[2,1,5,12,23,56,9,6,0,4,3]
# for i in range(0,len(a)):
# 	for j in range(0,i):
# 		if a[i]>=a[j]:
# 		    t=a[i]
# 		    a[i]=a[j]
# 		    a[j]=t
# print(a)
#例7
# 定义了支持参数收集的函数
# def test(a,*books):
#     print(books)
#     #books被当成元组处理
#     for b in books:
#         print(b)
#     #输出变量a的值
#     print(a)
# #调用test函数
# test(5 , "C语言中文网" , "Python教程")
#例8
# def test1(*book,nums):
#     print(book)
#     for bb in book:
#         print(bb)
#     print(nums)
# test1("java",'python',nums=20)
#test() 函数的第一个参数就是个数可变的形参，由于该参数可接收个数不等的参数值，因此如果需要给后面的参数传入参数值，
# 则必须使用关键字参数，否则程序会把所传入的多个值都当成是传给 books 参数的。

#例9
# def TEST(x,y,z=3,*bb,**score):
#     print(x,y,z)
#     print(bb)
#     print(score)
# TEST(2,3,4,'ruby','javascript',语文=89,数学=90)
#用 test() 函数时，前面的 1、2、3 将会传给普通参数 x、y、z；接下来的两个字符串将会由 books 参数收集成元组；
# 最后的两个关键字参数将会被收集成字典
'''
逆向参数收集：
a.所谓逆向参数收集，指的是在程序己有列表、元组、字典等对象的前提下，把它们的元素“拆开”后传给函数的参数。
b.逆向参数收集需要在传入的列表、元组参数之前添加一个星号，在字典参数之前添加两个星号
'''
#例10
# def test(name, message):
#     print("用户是: ", name)
#     print("欢迎消息: ", message)
# my_list = ['孙悟空', '欢迎来C语言中文网']
# test(*my_list)
#程序中定义了一个需要两个参数的函数，而 my_list 列表包含两个元素，为了让程序将 my_list 列表的两个元素传给 test() 函数，
# 程序在传入的 my_list 参数之前添加了一个星号

#例11实际上，即使是支持收集的参数，如果程序需要将一个元组传给该参数，那么同样需要使用逆向收集。例如如下代码
# def foo(name, *nums):
#     print("name参数: ", name)
#     print("nums参数: ", nums)
# my_tuple = (1, 2, 3)
# # 使用逆向收集，将my_tuple元组的元素传给nums参数
# foo('fkit', *my_tuple)
# # 使用逆向收集，将my_tuple元组的第一个元素传给name参数，剩下参数传给nums参数
# foo(*my_tuple)
# #如果不使用逆向收集（不在元组参数之前添加星号），整个元组将会作为一个参数，而不是将元组的元素作为多个参数。
# # 例如按如下方式调用 foo() 函数：
# # 不使用逆向收集，my_tuple元组整体传给name参数
# foo(my_tuple)
#例12字典也支持逆向收集，字典将会以关键字参数的形式传入
# def bar(book, price, desc):
#     print(book, "VIP价格是:", price)
#     print('描述信息', desc)
# my_dict = {'price': 159, 'book': 'C语言中文网', 'desc': '这是一个精美而实用的网站'}
# # 按逆向收集的方式将my_dict的多个key-value传给bar()函数
# bar(**my_dict)
'''
函数参数传递机制：
1.这是由 Python 函数的参数传递机制来控制的。Python 中函数的参数传递机制都是“值传递”。所谓值传递，就是将实际参数值的副本
（复制品）传入函数，而参数本身不会受到任何影响
2.如果需要让函数修改某些数据，则可以通过把这些数据包装成列表、字典等可变对象，然后把列表、字典等可变对象作为参数传入函数，
在函数中通过列表、字典的方法修改它们，这样才能改变这些数据
'''
#例13
# def swap(a,b):
#     a,b=b,a
#     print('a=',a)
#     print('b=',b)
# a=6
# b=9
# swap(a,b)
# print("交换结束后a是",a,'b是',b)

#例14
# def swap(dw):
#     dw['a'],dw['b']=dw['b'],dw['a']
#     print('dw[a]',dw['a'])
#     print('dw[b]',dw['b'])
# dw={'a':6,'b':9}
# swap(dw)
# print('交换后：')
# print('dw[a]', dw['a'])
# print('dw[b]', dw['b'])
'''
变量作用域：
根据定义变量的位置，变量分为两种：
局部变量：在函数中定义的变量，包括参数，都被称为局部变量。
全局变量：在函数外面、全局范围内定义的变量，被称为全局变量。
局部作用域：局部变量只能在局部使用
全局作用域：定义在函数外的变量，作用域是整个代码段
嵌套作用域：函数里面嵌套函数，内部函数可以使用外部函数的变量
作用域相关的关键字：当内部作用域想修改外部作用域的变量时，就要用到global即函数内定义全局变量;如果要修改嵌套作用域（enclosing 作用域，外层
非全局作用域）中的变量则需要 nonlocal 关键字了
注：　在函数内部，可以引用全局变量；如果全局和局部都有一个变量，函数查找，由内而外，局部没有，再到全局找
'''
# age=19
# def fun1():
#     global age
#     def fun2():
#         print(age)
#     fun2()
#     age=73
# fun1()
# print(age)
# class variable:
#     a='我是类变量'
#     def showvariable(self):
#         b='我是函数变量'
#         #print(a)#毫无疑问，编译器就已经报错了，这是因为类中的变量不可以在函数中直接访问
#         print(variable.a)#
#         print(self.a)
#         print(b)
# variable().showvariable()
# a='我是全局变量'
# def showvariable():
#     b='我一直是局部变量'
#     print(a)
#     print(b)
# def showb():
#     print(b)#报错，不能访问局部变量
# showvariable()
# showb()

'''
python内置函数：python内置了一系列的常用函数，以便于我们使用，python英文官方文档详细说明
python导入函数和模块：使用import 关键字，可以将一个包中已出现的一个或多个函数或模块，引入到另一个python代码中，从而实现
代码的复用
注意
1， 如果是本地导入文件，直接使用：import filename
2， 如果导入的是一个包，该包下面必须是有__init__.py文件才可以导入，否则报错，只有有了__init__.py文件，python解析器才
会把这个目录当成是的包
3.在导入的时候，.py的后缀直接省略，如果是多级的包，或者想导入包里面的函数等，可以使用from进行导入
from pack.mod_2 import Func2
Func2()
4.比如要引用模块 math，就可以在文件最开始的地方用 import math 来引入。在调用 math 模块中的函数时，必须这样引用：
模块名.函数名

'''
# Money = 2000
# def AddMoney():
#     # 想改正代码就取消以下注释:
#     global Money
#     Money = Money + 1
#     print(Money)
# AddMoney()
# print(Money)

