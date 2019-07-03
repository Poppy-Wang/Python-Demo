#coding=utf-8
'''
分支结构:1.用于实现根据条件来选择性地执行某段代码,,代码的缩进为一个 tab 键，或者 4 个空格 —— 建议使用空格,不要混用tab和空格键
        2.条件满足才能做某件事，不满足就做另一件事，即判断句，又称为分支语句，正因为有了判断才会有很多的分支结构
if语句:1.格式：if 要判断的条件:
                    条件成立时，要做的事情
              ......
              else:
                    条件不成立时，要做的事情
              ……
      2.缩进：if 和 else 语句以及各自的缩进部分共同是一个 完整的代码块，必须按 Python 语法要求缩进，if ,else,elif后的代码没有使用缩进就不是条件下的代码块，执行时可能会报错
              同一个代码中的缩进保持一致，否则会报错，对于不需要缩进的地方如果缩进，执行后也会报错
      3.if 分支使用布尔表达式或布尔值作为分支条件来进行分支控制，if 分支既可作为语句使用，也可作为表达式使用
      4.Python 的 if 语句有如下三种形式：a.if
                                       b.if......else
                                       c.if......elif......else
      5.从 Python 语法解释器的角度来看，Python 冒号精确表示代码块的开始点这个功能不仅在条件执行体中如此，后面的循环体、方法体、类体全部遵守该规则。
      6.Python 执行 if 语句时，会判断 if 条件是 True 还是 False，if 条件可以是任意类型，各种代表“空”的 None、空字符串、空元组、空列表、空字典都会被当成 False 处理
      7.if嵌套：   if 条件:
                    if 条件:
                        ..
                  else:
                    if 条件:
                        ...
'''
#例1
# age=int(input("请输入你的年龄"))
# if age>20:
#     print("年龄已经大于20岁了")
# else:
#     print("年龄小于20岁")
#
# #例2
# s=''
# if s:
#     print("s不是空字符串")
# else:
#     print("s是空字符串")
# my_list=[2,3]
# if my_list:
#     print("list不是空列表")
# else:
#     print("list是空列表")
# #例3
# day=int(input("今天星期几"))
# if day==1:
#     print("今天开工")
# elif day>=2 and day<=5:
#     print("继续工作")
# elif day==6 or day==7:
#     print("世界这么大一起去看看")
# else:
#     print("一周就7天你想干什么")
# #例4
# num=int(input("请输入一个数字"))
# if num>=1:
#     if num<=9:
#         print("这个数在1-9之间")
#     else:
#         print("我不猜了")
# else:
#     print("请输入一个正确的数字")
'''
循环结构:循环结构用于实现根据循环条件重复执行某段代码,提供了 while、 for-in 循环，也提供了 break 和 continue 控制程序的循环结构
While循环：a.语法结构：初始语句
                      while 循环条件:
                        循环体
                        迭代语句
           b.while 循环在每次执行循环体之前，都要先对循环条件求值，如果循环条件为真，则运行循环体部分。从上面的语法格式来看，迭代语句总是位于循环体的最后，因此只有当循环体能成功执行完成时，while 循环才会执行迭代语句
           c.while 循环也可被当成分支语句使用，即如果循环条件一开始就为假，则循环体部分将永远不会获得执行的机会。
           d.在使用 while 循环时，一定要保证循环条件有变成假的时候：否则这个循环将成为一个死循环，永远无法结束这个循环
           e.while 循环的循环体中所有代码必须使用相同的缩进，否则 Python 也会引发错误
           f.while循环可以遍历元组和列表
'''
#例1
# count=0
# while count<10:
#     print("count：",count)
#     count+=1
# print("循环结束")
#例2
# count=0
# while count<10:
#     print("count:",count)
#     count_=1
# print("死循环")
#例3while循环遍历元组
# touple=('bob','jack','jane')
# i=0
# while i<len(touple):
#     print(touple[i])
#     i+=1
# 例4while遍历列表
# list=[1,2,3,4,5]
# j=0
# while j<len(list):
#     print(list[j])
#     j+=1
'''
for-in循环:a.for-in 循环专门用于遍历范围、列表、元素和字典等可迭代对象包含的元素
        b.语法格式:for 变量 in 字符串｜范围｜集合等：
                    statements
        c.for-in 循环中的变量的值受 for-in 循环控制，因此该变量也被成为循环计数器，该变量将会在每次循环开始时自动被赋值，因此程序不应该在循环中对该变量赋值。
        d.for-in 循环可用于遍历任何可选代对象,所谓可迭代对象，就是指该对象中包含一个 __iter__ 方法，且该方法的返回值对象具有 next() 方法。
        e.for-in 循环可用于遍历范围。例如使用 for-in 循环来计算指定整数的阶乘
        f.for-in循环可以用于遍历列表和元组，在使用 for-in 循环遍历列表和元组时，列表或元组有几个元素，for-in 循环的循环体就执行几次，针对每个元素执行一次，循环计数器会依次被赋值为元素的值
        g.for-in 循环遍历字典其实也是通过遍历普通列表来实现的:items()：返回字典中所有 key-value 对的列表;keys()：返回字典中所有 key 的列表;values()：返回字典中所有 value 的列表
'''
#例1计算阶乘
# s_max=int(input("请输入你要计算的阶乘："))
# result=1
# for num in range(1,s_max+1):
#     result*=num
# print(result)
#上面程序将会根据用户输入的数字进行循环。假如用户输入 7，此时程序将会构建一个 range(1,8) 对象（不包含 8），
# 因此 for-in 循环将会自动循环 7 次，在每次循环开始时，num 都会被依次自动赋值为 range 所包含的每个元素
#例2遍历元组
# troup=('abc','greece','while')
# for ele in troup:
#     print(ele)
#例3遍历列表
# sum=0
# list=[1,2,3,'abc','def',4]
# for ele in list:
#     if isinstance(ele,int):
#         sum+=ele
#     else:
#         print(ele)
# print(sum)
#isinstance() 函数，该函数用于判断某个变量是否为指定类型的实例，其中前一个参数是要判断的变量，后一个参数是类型。
#例4遍历字典
# my_dict={'语文':89,'数学':98,'英语':90}
# for key,value in my_dict.items():
#     print('key:',key)
#     print('value:',value)
# for key in my_dict.keys():
#     print('key:',key)
#     print('value:',my_dict[key])
# for value in my_dict.values():
#     print('value:',value)
'''
range类型：a.python range() 函数可创建一个整数列表，一般用在 for 循环中
           b.函数语法：range(start, stop[, step])
           c.参数说明：start表示从start 开始，默认是从 0 开始。例如range（5）等价于range（0， 5）
                      stop表示计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
                      step表示步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)                  
'''
#例1
# for i in range(10):
#     print(i)
# for j in range(1,11):
#     print(j)
# for k in range(2,17,2):
#     print(k)
# s='runnob'
# for m in range(len(s)):
#     print(s[m])
'''
循环中的分支结构：python循环中else用法
Python 的循环都可以定义 else 代码块，当循环条件为 False 时，程序会执行 else 代码块
循环的 else 代码块是 Python 的一个很特殊的语法（其他编程语言通常不支持），else 代码块的主要作用是便于生成更优雅的 Python 代码。
循环嵌套：Python 程序中，如果把一个循环放在另一个循环体内，那么就可以形成循环嵌套
循环嵌套既可以是 for-in 循环嵌套 while 循环，也可以是 while 循环嵌套 do while 循环，即各种类型的循环都可以作为外层循环，各种类型的循环也都可以作为内层循环。
假设外层循环的循环次数为 n 次，内层循环的循环次数为 m 次，那么内层循环的循环体实际上需要执行 n × m 次
循环嵌套就是把内层循环当成外层循环的循环休。只有内层循环的循环条件为假时，才会完全跳出内层循环，才可以结束外层循环的当次循环，开始下一次循环
'''
#例1
# for i in range(0,5):
#     j=0          #内层循环
#     while j<3:
#         print('i的值为%d,j的值为%d'%(i,j))
#         j+=1
#当进入嵌套循环时，循环变量 i 开始为 0，这时即进入了外层循环。
# 当进入外层循环后，内层循环把 i 当成一个普通变量，其值为 0。在外层循环的当次循环中，内层循环就是一个普通循环。
'''
break 和continue语句:控制循环结构
a.break 用于完全结束一个循环，跳出循环体。不管是哪种循环，
一旦在循环体中遇到 break，系统就将完全结束该循环，开始执行循环之后的代码。
b.continue 的功能和 break 有点类似，区别是 continue 只是忽略当次循环的剩下语句，
接着开始下一次循环，并不会中止循环；而 break 则是完全中止循环本身。

'''
#例1
# for i in range(0,10):
#     print('i的值是：',i)
#     if i==2:
#         break
#看到 i 循环到 2 时即结束，因为当 i 等于 2 时，在循环体内遇到了 break 语句，程序跳出该循环。
#例2对于带 else 块的 for 循环，如果使用 break 强行中止循环，程序将不会执行 else 块
# for i in range(0,10):
#     print('i的值是：',i)
#     if i==2:
#         break
# else:
#     print('else')
#例3
# exit_flag = False
# # 外层循环
# for i in range(0, 5) :
#     # 内层循环
#     for j in range(0, 3 ) :
#         print("i的值为: %d, j的值为: %d" % (i, j))
#         if j == 1 :
#             exit_flag = True
#             # 跳出里层循环
#             break
#     # 如果exit_flag为True，跳出外层循环
#     if exit_flag :
#         break
#例1
# for i in range(0,3):
#     print('i的值是:',i)
#     if i==1:
#         continue#忽略本次循环剩下的语句
#     print('continue后的输出语句')

#作业
#输入一个三位数判断是否是水仙花数：水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）
N=input("请输入一个三位数")
#print(len(N))
num=int(N)
if len(N)==3:
    a=num//100
    b=num%100//10
    c=num%100%10
    sum = a ** 3 + b ** 3 + c ** 3
    if sum==num:
        print(num,"是水仙花数")
    else:
        print(num,"不是水仙花数")
else:
    print('输入的数不合法')
print(a,b,c)
print(sum)


# 判断一个数是不是完美数：完全数（Perfect number），又称完美数或完备数，如果一个数恰好等于它的因子之和，则称该数为“完全数”
# for...in循环
number=int(input("请输入一个整数："))
sum=0
for j in range(1,number):
    if number%j==0:
        sum+=j
if sum==number:
    print(number,"是完美数")
else:
    print(number,"不是完美数")

# while循环
numb=int(input("请输入一个整数："))
s=0
k=1
while k<numb:
    if numb%k==0:
        s+=k
    k+=1
if sum==numb:
    print(numb,"是完美数")
else:
    print(numb,"不是完美数")
#Fibonacci数列:指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
# 在数学上，斐波纳契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
def f(N):
    if N==1 or N==2:
        return 1
    else:
        return f(N-1)+f(N-2)
m=int(input("请输入一个数"))
for N in range(1,m+1):
    print(f(N))