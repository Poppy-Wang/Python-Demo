'''
字符串
1.字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。
2.建字符串很简单，只要为变量分配一个值即可。例如：var1='hello',var2="world"
3.Python 访问子字符串中的值，可以使用方括号来截取字符串,如例1
4.通过内置方法len()来计算字符串的长度，如例2
5.python字符串是不可以改变的序列，所有的序列都可以通过索引来获取其中的数据元素,格式如下：
    字符串【整数索引】
  说明：a.序列的正向索引是从0开始的，第二个索引为1,最后一个索引为 len(s)-1
        b.序列的反向索引是从-1开始的，-1代表最后一个，-2代表倒数第二个，以此类推，第一个是 -len(s)
   见例3
6.字符串的切片：从字符串序列中取出相应的元素重新组成一个字符串序列，格式如下：
    a.s[开始索引：结束索引：步长]---步长可以省略
    b.开始索引是切片切下的位置，0代表第一个元素，1代表第二个元素， -1 代表最后一个元素
    c.结束索引是切片的终止索引（但不包含终止点）
    d.步长是切片每次获取完当前元素后移动的方向和偏移量:没有步长，相当于步长为1,（默认为1） ;
        当步长为正整数时，取正向切片，开始索引默认为0，结束索引为最后一个元素的下一个位置 ;
        当步长为负数时，取反向切片, 反向切片时，默认的其实位置为最后一个元素，终止位置为第一个元素的前一个位置
    见例4
7.字符串常用方法：
a.将每个单词的首字母转大写：title()
b.大小写转化：upper();lower()---见例5
c.find 方法是用于在字符串中查找子串，如果找到，就返回子串的第一个字符的索引，否则返回-1.
  如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回
  开始的索引值，否则返回-1。见例6
d.count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置--见例7
e.Python endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则
    返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
    str.endswith(suffix[, start[, end]])---见例8
f.Python index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束）
    范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在
    string中会报一个异常。
    str.index(str, beg=0, end=len(string))
g.Python istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写--见例9
h.Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串--见例10
    str.join(sequence)
i.Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
    str.split(str="", num=string.count(str)).
    str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    num -- 分割次数。默认为 -1, 即分隔所有。
    --见例11
j.Python title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写

'''
#例1
# var1='Hello World'
# var2='Runoob'
# print('var1[1]=',var1[1])
# print('var2[0]=',var2[0])

#例2
# var1='Hello'
# var2=' World'
# print(len(var1))
# print(len(var2))

#例3
# s='abcd'
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print('--------')
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])

#例4
# s='abcdef'
# print(s[:4])
# print(s[:])
# print(s[2:])
# print(s[1:5:2])
# print(s[:6])#切片索引可以越界
# print(s[::2])
# print(s[-1:])
# print(s[::-1])
# print('-----')
# print(s[4:1:-1])
# print(s[-1::-1])

#例5
# s='hello World'
# print(s.title())
# print(s.upper())
# print(s.lower())

#例6
# s='my name is kk,my name is daodao'
# print(s.find('name'))
# print(s.find('is'))
# print(s.find('bobo'))
# print(s.find('name',7))
# print(s.find('name',5,22))

#例7
# s='my name is kk,my name is daodao'
# print(s.count('is'))
# print(s.count('is',9,17))

#例8
# str='my name is kk,my name is daodao'
# print(str.endswith('daodao'))
# print(str.endswith('kk'))
# print(str.endswith('daodao',7,17))

#例9
# str='This Is Python'
# str1='This is python'
# str2='THis Is Python'
# print(str.istitle())
# print(str1.istitle())
# print(str2.istitle())

#例10
# a=('a','b','c')
# s='-'
# print(s.join(a))

#例11
# txt = "Google#Runoob#Taobao#Facebook"
# txt1='a-b-c-d-e-f-g'
# # 第二个参数为 1，返回两个参数列表
# x = txt.split("#", 1)
# xx=txt.split('#',2)
# print(x)
# print(xx)
# print(txt1.split('-',3))

'''
列表：
1.创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可，如：
    list1 = ['Google', 'Runoob', 1997, 2000]
    list2 = ["a", "b", "c", "d"]
2.与字符串的索引一样，列表索引从0开始
3.使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符,访问列表时若下标越界
    则报错---见例1
4.可以使用append()方法在列表末尾来添加列表项;使用insert()方法在列表指定位置插入一个数；删除列表的的元素有三种方法：del 语句,remove(),pop();修改元素直接取列表中的一个元素然后重新赋值
    del 语句：dellist[start:end:step]，从列表中删除指定位置的元素根据索引(元素所在位置)来删除,既可删除列表中的单个元素，也可直接删除列表的中间一段,也可以直接删除变量
    remove():list.remove(元素),从列表中删除一个元素，且并不要求此元素的位置，只删除第一个找到的元素，如果找不到该元素，该方法将会引发 ValueError 错误
    pop(): list.pop(元素序号),无参情况下默认最后一个元素，并且返回该元素的值
    -----见例2
5.列表切片：list[start : end : step] ，start是切片起点索引，end是切片终点索引，但切片结果
    不包括终点索引的值。step是步长默认是1；在step的符号一定的情况下，start和end可以混合使用正向和反向索引，无论怎样，你都要保证

    start和end之间有和step方向一致元素 间隔，否则会切出空列表
6.列表的循环遍历：
    a.for循环遍历
    b.iter()迭代器：iter(object[, sentinel]) 函数用来生成迭代器，返回迭代对象。
        object -- 支持迭代的集合对象。
        sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），
        此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object。
    c.利用python内置函数enumerate（）列举出list中的数
        enumerate(sequence, [start=0])，返回枚举对象
        sequence -- 一个序列、迭代器或其他支持迭代对象。
        start -- 下标起始位置
    d.使用range（）函数:range(start, stop[, step]) ,不包括 end
    ---见例3
7.列表排序和倒序：a.sort()会自动按照字母顺序对字符串由小到大排序，如果数字就由小到大
                list.sort( key=None, reverse=False)
                key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
                reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
                注：sort（）会修改原来的列表他是修改列表，而不是创建新的列表,所以不能
                print(list.sort())
                b.sorted() 函数对所有可迭代的对象进行排序操作；sort 是应用在 list 上的方法，
                sorted 可以对所有可迭代的对象进行排序操作
                sorted(iterable, key=None, reverse=False)
                iterable -- 可迭代对象。
                key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
                reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
                c.reverse() 函数用于反向列表中元素。list.reverse()
                ----见例4
8.index() 函数用于从列表中找出某个值第一个匹配项的索引位置  
    index()方法语法：
    list.index(x[, start[, end]])    
    x-- 查找的对象。
    start-- 可选，查找的起始位置。
    end-- 可选，查找的结束位置。  
9.copy() 函数用于复制列表
    list.copy()返回一个一样的新列表
10.生成列表：a.python里面[]表示一个列表，快速生成一个列表可以用range()函数来生成
            b.列表生成式,如果想对列表里面的数据进行运算后重新生成一个新的列表，
            如[11, 22, 33 ... 1010],按平常思维就是先定义一个列表c，然后for循环挨个运算，算完了再append添加到c,最后c就是新的列表了
            c.列表生成式语法是固定的，[]里面for 前面是对列表里面数据的运算操作，后面跟
            平常for循序一样遍历去读取。运行后会自动生成新的列表
            ---见例5
11.python元组：a.Python的元组与列表类似，不同之处在于元组的元素不能修改。
              元组使用小括号，列表使用方括号。
              元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
              tup1 = ('physics', 'chemistry', 1997, 2000)
              tup2 = (1, 2, 3, 4, 5 )
              元组中只包含一个元素时，需要在元素后面添加逗号
              tup3=(50,)
              b.元组与字符串类似，下标索引从0开始，可以进行截取，组合等。
              元组可以使用下标索引来访问元组中的值
              c.元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
              d.元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
              e.因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中
              的一段元素
              L = ('spam', 'Spam', 'SPAM!')
              f.无关闭分隔符:任意无符号的对象，以逗号隔开，默认为元组
              g.len(tup)用于计算元组的个数
              h.Python 元组 tuple() 函数将列表转换为元组：tuple( seq )，seq为要转换成元组的序列
                针对字典 会返回字典的key组成的tuple
                元组会返回元组自身
              ----见例6
'''
#例1
# list=[1,'a','b',3,'c']
# print('list[0]=',list[0])
# print('list[1:4]=',list[1:4])
# print('list[5]',list[5])

#例2
# list=[1,2,3,4,5,6,7,8,9]
# list.append('a')
# list.append('b')
# list.append('c')
# print(list)
# del list[11]
# print(list)
# list.remove(5)
# print(list)
# list.pop(1)
# print(list)
# list[0]=11
# print(list)

#例3
# list=[1,2,3,4,5]
# for i in list:
#     print(i)
# print('-----')
# for i in iter(list):
#     print(i)
# print('----')
# for i in enumerate(list):
#     print(i)
# print('---')
# for i in range(len(list)):
#     print(list[i])

#例4
# list=['af','dg','ct','se','lu']
# list1=['af','dg','ct','se','lu']
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# sorted(list)
# print(list)
# list1.reverse()
# print(list1)

#例5
#range()
# b=range(1,11)
# print(b)#直接打印b会显示range(1, 11)对象，并不是直接显示应该列表，如果想显示列表，可以用list()转下
# print(list(b))
# c=[]
# for i in b:
#     c.append(i*i)
# print(c)
# d=[x*x for x in range(1,6)]
# print(d)
# #带if判断的列表生成器
# list1=[1, 3, -3, 4, -2, 8, -7, 6]
# list2=[x for x in list1 if x>0]
# print(list2)
# #前面列表生成式都只传一个参数x,如果有两个列表如何去运算呢?
# # a = [1, 2, 3, 4, 5]
# # b = ["a", "b", "c", "d", "e"]
# # 如何得出c = ["a1", "b2", "c3", "d4", "e5"]
# a = [1, 2, 3, 4, 5]
# b = ["a", "b", "c", "d", "e"]
# dd=[str(x)+str(y) for x,y in zip(b,a)]
# print(dd)

#例6
#访问元组元素
# tup=(1,2,3,4,5,6)
# print(tup[1])
# print(tup[5])
# #元组元素不可修改可以组合
# tup1=(1,2,3)
# tup2=('a','b')
# tup3=tup1+tup2
# tup11=tup1*4
# tup22=tup2*4
# print(tup3)
# print(tup11)
# print(tup22)
# #元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
# tup4 = ('physics', 'chemistry', 1997, 2000)
# print(tup4)
# del tup4
# #print('after del',tup4)#以上实例元组被删除后，输出变量会有异常信息
# #截取元组中的数
# tup5=(1,2,3,4,5,6,7,8,9)
# print(tup[1:5])#不包括最后一个
# print(tup5[:4])
# print(tup5[1:6:2])
# print(tup5[6:2:-2])
# #任意无符号的对象，以逗号隔开，默认为元组
# a='a','b','v','g'
# print(a)#输出a为元组
# #列表和元组的相互转换
# list=[1,2,3,4]
# list1={'a':1,'b':2}
# print(tuple(list))
# print(tuple(list1))#针对字典 会返回字典的key组成的tuple

'''
字典：1.字典是另一种可变容器模型，且可存储任意类型对象。
      2.字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，
      整个字典包括在花括号 {} 中 ,格式如下所示：
      d = {key1 : value1, key2 : value2 }
      3.键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一;
      值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组，用列表就不行
      4.访问字典里的值：把相应的键放入熟悉的方括弧；如果用字典里没有的键访问数据，会输出错误
      5.向字典添加新内容（更新）的方法是增加新的键/值对如：dic['a']=9；update() 函数把
        字典dict2的键/值对更新到dict里:dict.update(dict2)
      6.删除字典中的元素：del 永久删除；pop(key,default)删除指定的元素,key必须给出，
        否则返回默认值
      ----见例1
      7.Python 字典(Dictionary) clear() 函数用于删除字典内所有元素,dic.clear()
      8.字典的setdefault()，get()方法：键不存在于字典中，将会添加键并将值设为默认值
        dict.setdefault(key, default=None)
        dict.get(key, default=None)
        key -- 字典中要查找的键。
        default -- 如果指定键的值不存在时，返回该默认值值
      ---见例2
      9.keys()方法 / values()方法 / items()方法
        Python 字典(Dictionary) keys() 函数以列表返回一个字典所有的键：dict.keys()
        Python 字典(Dictionary) values() 函数以列表返回字典中的所有值:dict.values()
        Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组:dict.items()
        ----见例3
        
'''
#例1
#键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一
#键必须是不可变的，如字符串，数字或元组，用列表就不行
# dic={'a':1,'b':2,'c':2}
# #dic1={'a':1,'b':2,'b':3}
# dict1={'kecheng':'语文'}
# dic.update(dict1)
#print(dic)
# dict2={'课程':'chemistery','分数':90}
# dict5={1:'a',2:'r'}
# dict6={(4,):'aa'}
# # dict7={['Name']:'jack'}
# # print(dict7[['Name']])#key不能是list
# print(dict6[(4,)])
# print(dic)
# print(dic1)
# print(dict5[1])
# #访问列表中的值
# print(dic['a'])
# print(dict2['课程'])
# #字典中添加（更新）元素
# dict3= {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dict3['score']=90
# dict3['school']='小学'
# print(dict3)
# dict3['Name']='H&M'
# print(dict3)
# #删除字典中的元素
# dict4= {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print(dict4)
# print('---')
# #del dict4#永久删除，字典为空字典不再有值
# #print(dict4)
# print(dict4.pop('Name','HM'))
# print(dict4.pop('Score',90))

#例2
# dict = {'runoob': '菜鸟教程', 'google': 'Google 搜索'}
# print(dict.setdefault('runoob','python'))
# print(dict.setdefault('taobao','淘宝'))
# print(dict.get('google','python'))
# print(dict.get('jingdong','京东'))

#例3
# dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
# dict1={'a':1,'b':2}
# print('key值:%s'% dict.keys())
# print('values值:%s'%dict.values())
# for key,value in dict1.items():
#     print('key值：%s'%key)
#     print('value值%s'%value)

'''
集合：集合（set）是一个无序的不重复元素序列
1.可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，
    因为 { } 是用来创建一个空字典
    创建格式：parame = {value01,value02,...}
             或者
             set(value)
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    a = set('abracadabra')
    ---见；例1
2.添加/删除/清空元素：s.add( x )——将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作
                    s.update( x )也可以添加元素，且参数可以是列表，元组，字典等        
                    s.remove(x)将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误
                    s.discard( x )移除集合中的元素，且如果元素不存在，不会发生错误
                    s.pop()也可以设置随机删除集合中的一个元素,不可指定参数，否则报错
                    s.clear()清空集合
                    x in s 判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。
                    ----见例2
3.len()计算集合的元素个数
4.集合之间的运算：交集：a&b集合a和b中都包含了的元素
                 并集：a|b集合a或b中包含的所有元素
                 差集：a-b集合a中包含而集合b中不包含的元素
                 对称差：a^b不同时包含于a和b的元素
                 子集：z.issubset(x) z是x的子集,返回bool值
                 超集：x.issuperset(z) x是z的超集,返回bool值,即z是x的子集
             ---见例3
'''
#例1
# params={'a','b','c'}
# a=set(('aa','bb','cc'))
# b=set('abc')
# print(a)
# print(b)
#例2
# thisset = set(("Google", "Runoob", "Taobao"))
# print('添加之前集合：',thisset)
# thisset.add('facebook')
# print('添加之后集合：',thisset)
# thisset.update(['baidu'])#参数可以是列表，元组，字典等
# print('updfate更新后集合:',thisset)
# thisset.remove('baidu')#移除已经存在
# print('移除后：',thisset)
# #thisset.remove('jd')#移除不存在的报错
# #print(thisset)
# print('-----')
# thisset.discard('jd')#移除不存在的不报错
# print(thisset)
# thisset.discard('Taobao')#移除已经存在的
# print(thisset)
#随机删除
# sets=set(('1','2','3','4','5','6'))
# sets.pop()
# print(sets)
# sets.pop()
# print(sets)
#print(len(sets))
#sets.clear()
#print(sets)
#print('3' in sets)

#例3
#交集
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print('----')
print(a&b)
#并集
print(a|b)
#差集
print(a-b)
#对称差集
print(a^b)
#子集
print('-----')
c=set('12345')
d=set('123')
e=set('1236')
print(d.issubset(c))
print(e.issubset(c))
#超集
print(c.issuperset(d))
print(c.issuperset(e))