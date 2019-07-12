'''
python面向对象：面向对象编程是一种编程方式，此编程方式的落地需要使用 “类” 和 “对象” 来实现，所以，面向对象编程其实就是对 “类” 和 “对象” 的使用
1.类：用来描述具体相同的属性和方法的对象的集合。定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
2.方法：类中定义的函数
3.类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
4.数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
5.方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
6.局部变量：定义在方法中的变量，只作用于当前实例的类。
7.实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
8.继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
9.实例化：创建一个类的实例，类的具体对象。
10.对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
注：1.类就是一个模板，模板里可以包含多个函数，函数里实现一些功能
    2.对象则是根据模板创建的实例，通过实例对象可以执行类中的函数
格式：
class Pro: class 是关键字，表示创建类，Pro是新建类的名称
    #创建类中的函数（方法）
    def bar(self):      #self特殊参数必填,第一个参数
        pass
#根据类Pro创建类对象obj
---见例1
obj=Pro()
11.类的基本结构：class ClassName:
                <statement-1>
                 .
                 .
                 .
                <statement-N>
    1）类实例化后，可以使用其属性，实际上，创建一个类之后，可以通过类名访问其属性
    2）类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法
    3）在python3中，所有类最顶层父类都是object类
    4）加object和不加的区别：例如class Person()和class Animal(Object)两个类，Person类很明显能够看出区别，不继承object对象，
        只拥有了__doc__ , __module__ 和 自己定义的name变量, 也就是说这个类的命名空间只有三个对象可以操作.
        Animal类继承了object对象，拥有了好多可操作对象，这些都是类中的高级特性
                        class Person:
                    """
                    不带object
                    """
                    name = "zhengtong"


                        class Animal(object):
                            """
                            带有object
                            """
                            name = "chonghong"

                        if __name__ == "__main__":
                            x = Person()
                            print "Person", dir(x)

                            y = Animal()
                            print "Animal", dir(y)
                输出：Person ['__doc__', '__module__', 'name']
                     Animal ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', 
                                 '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
                                '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']
                注：实际上在python 3 中已经默认就帮你加载了object了（即便你没有写上object）
12.类的属性：
    1）可以使用点(.)来访问对象的属性
    2）也可以使用以下函数的方式来访问属性：
        getattr(obj, name[, default]) : 访问对象的属性
        hasattr(obj,name) : 检查是否存在一个属性
        setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性
        delattr(obj, name) : 删除属性
    3）Python内置类属性
        __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
        __doc__ :类的文档字符串
        __name__: 类名
        __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
        __bases__ : 类的所有父类构成元素（包含了以个由所有父类组成的元组）
13.类的方法：
    1）在类的内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self，且为第一个参数
    2）类的专有方法：
        __init__ 构造函数，在生成对象时调用：初始化函数，用来完成一些默认的设定
        __del__ 析构函数，释放对象时使用
        __repr__ 打印，转换
        __setitem__按照索引赋值
        __getitem__按照索引获取值
        __len__获得长度
        __cmp__比较运算
        __call__函数调用
        __add__加运算
        __sub__减运算
        __mul__乘运算
        __div__除运算
        __mod__求余运算
        __pow__称方
        __init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法，与c++中构造函数类似。只需在自定义的类中重写__init__()方法即可。
    3）实例方法：只能通过实例调用，实例方法第一个定义的参数只能是实例本身引用---见例2
    4) 类方法：定义类方法，要使用装饰器@classmethod,定义的第一个参数是能是类对象的引用，可以通过类或者实例直用---见例3
                class main:
                    @classmethod
                    def run(cls, arg1, arg2, ...):cls（必须） - 当前类本身 arg1,arg2 - 自定义参数
                         ...
        @classmethod:函数装饰器的主要作用是将一个类的普通方法（需要实例化使用）声明为一个类方法（可以直接使用类名调用）。
                    在类的功能扩展（包括功能的整合以及类的继承），代码整洁度，后期的可维护性起到一定的帮助。虽然类方法也可以在实例化后，
                    使用实例化对象进行调用，但这是不赞成的，因为这样会容易将它和普通的实例化方法混淆，后期代码不利于维护。
                    具体是否使用以及其是方法方式还需要根据业务的实际需要决定。
                    它是Python的内置函数，在python文件中直接可以使用。它只能被应用在类（class）中
        a.@classmethod的使用方法---实例1
        b.@classmethod的使用场景之代码整合：有时我们可能会遇到一些情况，在创建类的时候只有一种可能性，但是在实际业务发展过程中将演变出多种可能性，
                                            这时需要在外部处理好参数，然后再实例化类，将参数传递给类。如果多个模块调用这个类，必然会产生一定的混乱。
                                            如果将这个处理过程以一个普通方法的方式编写在类中，又必须先实例化类，然后才能调用，但是这样会导致先触发
                                            类的初始化方法__init__()以及__repr__()、__set__()等等。可是我们的类是需要先把参数处理好，然后才能初始化，
                                            否则会出问题的，这可能导致整个类的业务逻辑方式改变。造成大量的修改。
                                            ---实例2
        c.@classmethod使用场景之类的重载----实例3
    4）静态方法:定义静态方法使用装饰器@staticmethod,没有默认的必须参数，通过类和实例直接调用---见例4
    5）property装饰器
14.类变量和实例变量：类的属性有两种作用域：类变量，实例变量。Python中是不支持静态变量的，但是我们可以通过函数的默认值来实现静态变量的功能
    a.类变量紧接在类名后面定义,class里def外，通过变量名能被赋值
    b.实例变量在__init__里定义,def里通过self点运算变量名能被赋值，不一定非在init里，其他已被调用的方法函数里也行
    c.类变量属于整个class所共享，而实例变量则仅仅属于特定对象实例
    class Dog:
    kind = 'canine'
        def __init__(self, name):
            self.name = name
    类Dog中，类属性kind为所有实例所共享；实例属性name为每个Dog的实例独有

15.__str__方法:当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据;
                __str__方法需要返回一个字符串，当做这个对象的描写;
                在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
                ----实例4
16.析构/构造函数：构造函数---------------------   __init__( self )：构造函数在类的构造的时候调用，但是不是一定会调用
                  析构函数---------------------  __del__( self )

                   析构函数：__del__(self)
                                     在程序全部结束时自动结束，当程序无法结束时该函数也不会执行。

                   执行时间：1.如果该析构函数是全局，则程序结束自动执行
                          2.如果该析构函数是局部，比如在函数中，函数执行完毕后就自动执行
                          3.手动删除   del+变量名，删除后不能再次使用。
                   析构函数的意义：

                                 其实析构函数大部分时间作用不大，要说它比较有用的地方便是当你

                                 看到你写的析构函数打印出来的时候就代表着该程序块或者该函数已经全部执行结束了，

                                 所以大部分时间都处于无用的地位
                            见例5


面向对象三大特征：封装，继承，多态
'''
#例1
# class Pro():
#     def Bar(self):
#         print('bar')
#     def sayHi(self,name):
#         print('Hello,%s'%name)
# obj=Pro()
# obj.Bar()
# obj.sayHi('Python')

#例2
# class Myclass:
#     def foo(self):
#         print(id(self),'foo')
# a=Myclass()#既然是实例对象，那就要创建实例
# a.foo()#输出类里的函数地址
# print(id(a))#输出类对象的地址

#例3
# class Myclass:
#     @classmethod#类装饰器
#     def foo2(cls):#cls类装饰器参数
#         print(id(cls),'foo2')
#    #类对象，直接可以调用，不需要实例化
# print(id(Myclass),'yy')
# Myclass.foo2()#直接可以调用

#例4
# class Myclass:
#     @staticmethod#静态方法，定义静态方法使用装饰器@staticmethod,没有默认的必须参数
#     def foo3():
#         print('foo3')
# Myclass.foo3()#没有参数，类对象
# a=Myclass()#实例对象
# a.foo3()

#例5
# class Person:
#     def __init__(self):
#         print('111')
#     # def __new__(cls,self):
#     #     print('333')
#     def __del__(self):#__del__方法：垃圾回收机制,当没有任何变量引用对象时，才启动垃圾回收机制;
#         # 这个函数要直到该实例对象所有的引用都被清除掉后才会执行
#         print('222')
#     def eat(self):
#         print('吃')
# p=Person()
# p.eat()

#实例1
# class main:#声明类
#     #普通方法
#     def set(self,x):
#         print(x)
#     #类方法
#     @classmethod
#     def run(cls,n):
#         print(n)
# #普通方法需要实例化后调用
# obj=main()
# obj.set('abc')
# #类方法可以直接使用，不需要实例化
# main.run(6)

#实例2
# class Date:#创建类
#     def __init__(self,year,month,day):#初始化
#         self.year=year
#         self.month=month
#         self.day=day
#     def print_date(self):
#         print(self.year, self.month, self.day)
# #实例化类
# data_object = Date('2018','10','31')
# data_object.print_date()
#在上面的例子中可以看到类的实例化需要传递‘年月日’三个参数。并且是要求分别传递。那么假设用户不按照要求填写，他填写的2018-10-31这样的一个参数呢？
#我们需要先对参数进行分割处理，然后再实例化类。例如下面的代码：
#分割函数
# def from_string(date_as_string):
#     return map(int, date_as_string.split('-'))
# #创建类
# class Date(object):
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#     def print_date(self):
#         print(self.year, self.month, self.day)
# #先执行分割函数对数据进行处理
# year, month, day = from_string('2018-10-31')
# #实例化类
# data_object = Date(year, month, day)
#执行输出函数
#data_object.print_date()
#这样做视乎可以解决这个问题，但是from_string方法应该是属于类的一部分，现在需要写在外部，就导致了类功能外散，后期不便于管理，
# 以后增加功能的时候会出现问题，所以我们就必须将from_string迁移到类里面去，并且还要在类的实例化之前调用它，我们都知道，一般情况下，
# 如果想调用类中的方法，必须先实例化类，而我们现在的需求是要在实例化之前。这时就需要使用@classmethod咯。代码如下：
#创建一个类
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def print_date(self):
#         print(self.year, self.month, self.day)
#     @classmethod
#     def from_string(cls,date_as_string):
#         year, month, day = map(int, date_as_string.split('-'))
#         return cls(year, month, day)  # 实例化类并返回实例化对象
# data_object = Date.from_string('2018-10-31')
# print(data_object)
# #执行输出函数
# data_object.print_date()
#这是一个比较经典的案例，来自于stackoverflow。我暂时没有想到更好的，就先对原案例进行了一些修改并且加上了一些注释。
#使用@classmethod可以有效的防止类功能外散，可以将对属于当前类的功能集中起来，便于管理，并且对类的继承、重载、多态都是有一定的帮助，
# 这个小例子只能算是一个用法说明，在实际的操作中会有更加复杂的用法，还需要以项目的实际业务逻辑来制定。

#实例3
#声明一个类
# class main:
#     #声明类方法
#     @classmethod
#     def run(cls):
#         #调用name方法
#         cls.name()
#     #声明name类方法
#     @classmethod
#     def name(cls):
#         print('我是main类的name方法')
# #声明子类并继承main类
# class main2(main):
#     #重载基类的name方法
#     @classmethod
#     def name(cls):
#         print('我是main2类的name方法')
# main2.run()
#我是main2类的name方法
#输出结果是子类的重载name方法。因为cls指向的永远都是调用那个类

#实例4
# class Cat:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return "名字是:%s , 年龄是:%d" % (self.name, self.age)
#
#     def eat(self):
#         print("%s在吃鱼...." % self.name)
#
#     def drink(self):
#         print("%s在喝可乐..." % self.name)

# tom=Cat('jack',23)
# tom.eat()
# tom.drink()
# print(tom)

'''
python的属性：
1.类属性就相当与全局变量，实例对象共有的属性，实例对象的属性为实例对象自己私有；
    类属性就是类对象所拥有的属性，它被所有类对象的实例对象(实例方法)所共有，在内存中只存在一个副本；
    对于公有的类属性，在类外可以通过类对象和实例对象访问；
    __name，代表私有类属性
    使用方式：类名.类属性，也可以使用 对象名.类属性
    ---见例1
2.实例属性(对象属性)：实例属性属于各个实例所有，互不干扰；实例属性是在__init()方法中定义的属性---见例2
python属性访问器 / 属性修改器 / 属性删除器/property
1.我们通常要对属性进行获取(getter)，修改(setter)，删除(deleter)这些操作---见例3、例4
'''
#例1
# class Tool:
#     num=10#公有的类属性
#     # __age=10    不能在类外通过实例对象访问私有的类属性
#     def dig(self):
#         print('111')
# t=Tool();
# t.dig()
# print(t.num)
# print(t.__age)
#print(Tool.__age)#不能在类外通过类对象访问私有的类属性

#例2
# class Person:
#     address='山东'#类属性
#     def __int__(self,name,age):
#         self.name='11'#实例属性
#         self.age=22#实例属性
# p = Person()
# p.age =12 #实例属性
# p.name='xiaoming'
# print(p.address) #正确
# print(p.name)    #实例属性是实例对象特有的，类对象不能拥有
# print(p.age)     #实例属性是实例对象特有的，类对象不能拥有

#例3
# class Cls(object):
#     def __init__(self):
#         self.__x = None
#
#     def getx(self):
#         return self.__x
#
#     def setx(self, value):
#         self.__x = value
#
#     def delx(self):
#         del self.__x
#
#     x = property(getx, setx, delx, 'set x property')
# #在该类中定义三个函数，分别用作赋值、取值、删除变量
# #property函数原型为property(fget=None,fset=None,fdel=None,doc=None)，上例根据自己定义相应的函数赋值即可
#
# if __name__ == '__main__':
#     c = Cls()
#     c.x = 100
#     y = c.x
#     print("set & get y: %d" % y)
#
#     del c.x
#     print("del c.x & y: %d" % y)
#
#
# class Cls(object):
#     def __init__(self):
#         self.__x = None
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         self.__x = value
#
#     @x.deleter
#     def x(self):
#         del self.__x
#
#
# if __name__ == '__main__':
#     c = Cls()
#     c.x = 100
#     y = c.x
#     print("set & get y: %d" % y)
#
#     del c.x
#     print("del c.x & y: %d" % y)
#私有属性，我们只能通过访问器进行访问
# class Student():
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self,value):
#         self._score=value
#     @score.deleter
#     def score(self):
#         del(self._score)
# a=Student()
# a.score=2
# print(a.score)
# del(a.score)

#例4
# class Student(object):
#     def __init__(self):
#         self._name = None
#     @property
#     def name(self):         # 注意 这三个方法名要一样
#         return self._name
#     @name.setter                  # 注意 装饰器名改变
#     def name(self, value):  # 注意 这三个方法名要一样
#         self._name = value
#     @name.deleter                 # 注意 装饰器名改变
#     def name(self):         # 注意 这三个方法名要一样
#         del self._name
# student = Student()
# student.name = 'Li'   # 相当于 student.set_name('Li')
# print(student.name)        # 相当于 student.get_name
# del student.name      # 相当于  del student.name



### 实例2 ###
# class Student(object):
#     def __init__(self):
#         self._name = None
#
#     def get_name(self):  # 取属性
#         return self._name
#
#     def set_name(self, n):  # 修改/设置 属性
#         if not isinstance(n, str):  # 如果传入的不是字符串 抛出一个异常 可以避免属性接受非字符串对象
#             raise TypeError('Name must be str!')  # raise表达式用于抛出一个异常
#         self._name = n
# student = Student()
# student.set_name('li')  # 正确的设置属性
# student.get_name()  # 访问属性
# student.set_name(123)  # 错误的设置属性
'''
如果我们想要限制实例的属性怎么办？比如，只允许对Person实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：----见例1
'''
#例1
# class Person(object):
#     __slots__ = ("name", "age")#限制Person类的属性只有name 和 age
# P = Person()
# P.name = "老王"
# P.age = 20
# #P.score=120
# #使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# class Student(Person):
#     pass
# s = Student()
# s.name='1'
# s.age=12
# s.score=100
'''
类中的方法 - 实例方法 / 类方法 / 静态方法
1.静态方法：用 @staticmethod 装饰的不带 self 参数的方法叫做静态方法，类的静态方法可以没有参数，可以直接使用类名调用
2.类方法：默认有个 cls 参数，可以被类和对象调用，需要加上 @classmethod 装饰器
3.实例方法：即普通方法，默认有个self参数，且只能被对象调用
---见例1
'''
#例1
# class Classname:
#      country='55'
#      @staticmethod
#      def fun():
#          print('静态方法')
#      @classmethod
#      def a(cls,name):
#          print('类方法')
#          print(name)
#          print(cls.country)
#          cls.fun()#类方法调用静态方法，可以让cls代替类，
#      # 普通方法
#      def b(self):
#          print('普通方法')
# Classname.fun()
# Classname.a('333')
# #Classname.b()#类不能直接调用实例方法，必须通过一个类的实例去访问
# C = Classname()
# C.fun()
# C.a('44')
# C.b()

'''
对象的创建和使用
'''
# import math
#
# class Point:
#     def move(self, x, y):   # 接受x和y两个参数，并且给self对象赋值
#         self.x = x
#         self.y = y
#
#     def reset(self):  # 移动到特定位置的move
#         self.move(0, 0)
#
# # 接受另一个Point对象作为输入，返回距离
#     def calculate_distance(self, other_point):
#         return math.sqrt(
#                 (self.x - other_point.x) ** 2 +
#                 (self.y - other_point.y) ** 2)

# 如何使用它
# point1 = Point()
# point1.move(65,16)
# point2 = Point()
# print(point2.reset())
# r=point2.calculate_distance(point2)
# print(r)
'''
面向对象-封装
1.封装是是面向的特点之一,同时这也是最重要的,对象可以没有继承,可以没有多态,但是不能没有封装,没有封装的对象就不是一个合格的对象.
2.封装内分为属性和方法,初次接触的同学可能不太习惯,但是,不要紧.
3.你可以把属性想象成一个人的名字,年龄等信息,通常都是名词性质的,而方法想象成是一种行为,比如一个人吃饭,睡觉等,通常是具有动词性质的.
4.而属性和方法又有公有和私有的划分，以__开头是私有
5.把同一类的函数和变量放到一个类中去的过程叫做封装
'''
# class Cat:
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#
#     def run(self):
#         print("%s在跑，颜色是%s"%(self.name, self.color))
#
# c=Cat('emma', "gray")
# c.run()

# class stu():
#      def __init__(self, name, age, score):
#          self.__name = name
#          self.age = age
#          self.__score = score
# xiaoming = stu("xiaoming", 15, 90)
# print(xiaoming.age)
# print(xiaoming.name)


# class Person:
#     # 写构造函数  init(初始化)
#     # self.变量名----创建变量
#     # self--自己(谁调用self就代表谁)
#     # Person()---构造函数
#     def __init__(self):
#         self.name = None
#         self.age = None
#         self.sex = None
#         print('我出生了！')
#
#     # 普通函数
#     def eat(self):
#         name = '李四'
#         print(name, '吃饭')
# 创建对象（实例化对象）
# 创建对象默认调用构造函数
# p1 = Person()
# p1.name = '张三'
# p1.age = 22
# p1.sex = '男'
# p1.eat()
# print(p1.name, p1.sex, p1.age)


'''
面向对象—继承
1.子承父类，就相当于把一些公共方法封装成一个类，当需要用到这个类里面的功能，就继承该类就可以使用里面的功能了。子类继承了父类也可以使用父类的父类的功能。
私用方法或属性不能被继承。
2.重写：子类继承了父类时，如果你觉得父类的方法不是你想要的方法，
你可以在自己的类里面写一个和父类名字一模一样的方法名，把你想要的功能从新写入。既是重。
因为程序是先找子类有没有该方法，如果没有则到父类去找，如果有的话直接使用子类的方法。
3.多继承：一个子类继承多个父类
'''
# 创建a类继承object类(所有的类默认都是继承object类)
# class A(object):
#
#     def a_func(self):
#         print('这是a类的功能')
#
# # 创建b类，继承a类
# class B(A):
#
#     def b_func(self):
#         print('这是b类的功能')
# # 实例化a类（创建x对象）
# x = A()
# x.a_func()
#
# # 实例化b类（创建y对象）
# y = B()
# y.a_func()  # 调用父类的功能
# y.b_func()

#重写
# 创建a类继承object类(所有的类默认都是继承object类)
# class A(object):
#
#     def a_func(self):
#         print('这是a类的功能')
#
# # 创建b类，继承a类
# class B(A):
#
#     def b_func(self):
#         print('这是b类的功能')
#
#     # 重写父类方法
#     def a_func(self):
#         print('这是重写a类后的功能')

    # 子类重写了父类的功能，但还是想用父类的功能
    # def b_func2(self):
    #     A.a_func(self)    # 可以通过:父类名.被重写的方法名(self):调用
    #     A().a_func()      # 第二种调用方式
    #     super().a_func()  # 第三种调用方式


# 实例化a类（创建x对象）
# x = A()
# x.a_func()
#
# # 实例化b类（创建y对象）
# y = B()
# y.a_func()  # 此时调用的是被重写后的方法
# y.b_func()
# y.b_func2()

# class A(object):
#
#     def a_func(self):
#         print('这是a类的功能')
#
# # 创建b类
# class B(object):
#
#     def b_func(self):
#         print('这是b类的功能')
#
# # 创建c类型 继承a类和b类
# class C(A, B):
#
#     def c_func(self):
#         print('这是c类的功能')
# 创建z对象
# z = C()
# z.a_func()
# z.b_func()
# z.c_func()
#多继承类的方法调用顺序：首先，先找他自己的方法，如果没有则找第一个父类的方法，再找第二个父类的方法，直到object类

'''
面向对象—多态
1.作用：一个接口，多种实现
2.目的：接口的重（chong）用
3.多态的最基本的实现就是通过继承来实现的
'''
# class People(object):
#     def __init__(self, name):
#         self.name = name
#
# class Man(People):
#     def walk(self):
#         print('%s is walking' % self.name)
#
# class Woman(People):
#     def walk(self):
#         print('%s is walking' % self.name)
#
# man1 = Man('xiaoming')
# man1.walk()
# man2 = Woman('ruhua')
# man2.walk()
#简单的三个类，两个子类都继承了父类People，父类中有构造函数初始化name变量，两个子类中都有一个walk函数，实例化了两个对象man1和man2，
# 分别调用了walk函数，实现了输出这两句话
#但是我们能不能写一个函数，当作一个接口，传入对象就可以执行walk函数，而不是用这个对象来调用walk函数呢？
#继承是多态的前提
#创建父类
class People(object):
    def __init__(self, name):
        self.name = name
    @staticmethod#静态方法
    def people_walk(obj):
        obj.walk()

class Man(People):
    def walk(self):
        print('%s is walking' % self.name)

class Woman(People):
    def walk(self):
        print('%s is walking' % self.name)
#实例化
man1 = Man('xiaoming')
#man1.walk()
man2 = Woman('ruhua')
#man2.walk()
People.people_walk(man1)
People.people_walk(man2)


















