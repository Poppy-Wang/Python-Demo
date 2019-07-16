'''
python读取文件:
1.读写文件是最常见的IO操作。Python内置了读写文件的函数
2.要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：
    f = open(file, 'mode')
    file:必需，文件路径（相对或者绝对路径）
    mode:可选，文件打开模式,如'r','w',默认为文本模式，如果要以二进制模式打开，加上 b
    如果文件不存在，open()函数就会抛出一个IOError的错误
3.如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
4.最后一步是调用close()方法关闭文件
5.调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用
6.由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
    try:
        f = open('/path/to/file', 'r')
        print(f.read())
    finally:
        if f:
            f.close()
7.但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
    with open(file, mode) as f:
        print(f.read())
8.要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
    f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
    f.read()
'''
'''
python写文件：
1.写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
    f = open('/Users/michael/test.txt', 'w')
    f.write('Hello, world!')
    f.close()
2.可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件，忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。
所以，还是用with语句来得保险：
    with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
3.r+ 可读可写 ，如果我们在open文件后，没有进行任何读写，则从末尾加入,从顶部开始写 会覆盖之前此位置的内容不完整---例1
4.如果我们在写之前进行了读操作，则会在末尾加入文件---例2
5.如果以w+方式打开文件,写入文件后，文件被覆盖或重建，需要seek才能读取到刚刚写入的内容。---例3、4
6.读的一行末尾会有换行操作，可以用''.strip()去掉换行符---例5
'''
#例1
# test.txt的原始文件如下：
# 早上好
# 您好
# how are you?
# with open('test.txt', mode='r+', encoding='utf-8') as f:
#     f.writelines("北京")
# 这时文件变成
# 北京好
# 您好
# how are you?

#例2
# with open('test.txt', mode='r+', encoding='utf-8') as f:
#     f.read(1)
#     f.writelines("北京")
# 这时在文件的末尾加入了北京两个字
# 早上好
# 您好
# how are you?北京

#例3
# with open('test.txt', mode='w+', encoding='utf-8') as f:
#     f.write("tianjin")
#     f.flush()
#     print(f.readlines())
#得到[]

#例4
# with open('test.txt', mode='w+', encoding='utf-8') as f:
#     f.write("tianjin")
#     f.writelines('山东')
#     f.flush()
#     f.seek(0)
#     print(f.readlines())
#另外注意 写操作不会自动加入换行符

#例5
# with open('test.txt', mode='r', encoding='utf-8') as f:
#     for line in f:
#         print(line.strip())#去掉换行

'''
python异常处理
1.Python 有两种错误很容易辨认：语法错误和异常
2.大多数的异常都不会被程序处理，都以错误信息的形式展现在这里
3.try语句处理异常
    a.首先，执行try子句（在关键字try和关键字except之间的语句）
    b.如果没有异常发生，忽略except子句，try子句执行后结束。
    c.如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
    d.如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
    e.一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
    f.处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
    g.一个except子句可以同时处理多个异常
4.try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行
    for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
5.Python 使用 raise 语句抛出一个指定的异常
6.raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出
7.用户自定义异常:你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承
'''
# def this_fails():
#     x = 1 / 0
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)

# raise NameError('here')
# try:
#         raise NameError('HiThere')
# except NameError:
#         print('An exception flew by!')
#         raise

# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return repr(self.value)
# try:
#         raise MyError(2*2)
# except MyError as e:
#         print('My exception occurred, value:', e.value)
#不管 try 子句里面有没有发生异常，finally 子句都会执行。

'''
数据持久化:
1.python操作csv文件：
2.csv模块的应用：
3.json数据格式：
4.json模块的应用

'''