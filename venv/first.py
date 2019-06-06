# -*- coding: utf-8 -*-
import math
a = 5
b = 6
c = a + b
print("%d", c)
f = "hello the world"
print("%s", f)

print('I\'m ok')

print('\\\n\\')

print(r'\\\n\\')

print('''line1
line2
line3''')

print('Hello, %s' % 'world')

print('Hi, %s, you have $%d.' % ('kd', 100000))

print('%02d' % 3)

print('%.2f' % 3.1415)

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.256))


classmate = ['mic', 'bob', 'ked']
print('{}'.format(classmate[0]))

print('the name is %s' % classmate[0])

classmate.append('wd')

print('the last name is %s' % classmate[-1])

classmate.insert(1, 'kb')
print('the second name is %s' % classmate[1])

classmate.pop()
print('the last name is %s' % classmate[-1])

classmate.pop(1)
print('the second name is %s' % classmate[1])

L = ['apple', 123, True]
print('%s' % len(L))

t = (1, 2, 3)
print('the second no. is %s' % t[1])

t = ('a', 'b', ['d', 'e'])
print('the first is %s' % t[0])

t[2][0] = 'X'
t[2][1] = 'Y'
print('the last is %s' % t[2][1])

sum = 0
n = 99
while n>0:
    sum = sum+n
    n = n-2
print(sum)

s = set([1, 2, 3, 4])
print(s)

dd = {'ddd': 66, 'ccc': 77, 'eee': 88}
print(dd['ddd'])

dd['ggg'] = 77
print(dd['ggg'])

#help(abs)

abs(1)

a = abs
t = a(-1)
print(t)

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TabError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99.8))

def nopp():
    pass

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)

    return nx, ny

rrr = move(100, 100, 60, math.pi / 6)
print(rrr)

ll = [3, 4, 5]
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(*ll))

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'others:', kw)

def person1(name, age, *, city, job):
    print('name:', name, 'age:', age, 'others:', city)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('kevin', 25, **extra)


person1('jack', 65, city='bj', job='engineer')
L = list(range(100))
print(L)

print(L[::10])

ddc = {'a': 1, 'b': 2, 'c': 3}
for key, value in ddc.items():
    print(key, value)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in ([(1, 1), (2, 4), (3, 9)]):
    print(x, y)

s = [m + n for m in 'ABC' for n in 'XYZ']
print(s)

x = 'aabc'
y = 123
print(isinstance(x, str))
print(isinstance(y, str))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'

o = fib(10)
print(o)  #这个时候实际上是指向generator的地址
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
for n in fib(10):
    print(n)

def add(x, y ,f):
    return(f(x) + f(y))

print(add(5, 5, abs))

#试验map()
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7])
print(list(r))
print(r)   #由于map返回的时Iterator（迭代器），属于惰性序列，所以，直接print不会有
           #结果输出。因此，通过list()函数把整个序列都计算出来并返回一个list
print(list(map(str, [1, 2, 3, 4, 5, 6])))

#试验reduce函数
from functools import reduce
def add(x, y):
    return x + y
v = reduce(add, [1, 3, 5, 7, 9])
print(v)

#试验一个map & reduce
#实现str转成int
def fn(x, y):
    return x * 10 + y
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3,}
    return digits[s]
print(char2num('1'))
print(reduce(fn, map(char2num, '123')))

#试验lambda功能(匿名函数)
#lambda实际上就时代替了def定义函数功能。
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int('12'))

def normalize(name):
    dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',]
    for n in range(3):
        print(name[n])
   # for q in len(name[n])
    #    print
    return






L1 = ['adam', 'LISA', 'barT']
#L2 = list(map(normalize, L1
normalize(L1)

def str2asc(LL):  #该函数是能够将不规则的str转化成只有首字母为大写字母的str
    DDDD = []
    str = ''
    DDS = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'm': 'M'}
    DDQ = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'M': 'm'}
    n1 = LL[:1]
    yyy = DDS[n1]
    DDDD.append(yyy)
    print(n1)
    for n in range(len(LL)):  #range的作用是为了生成一个list
        a1 = LL[n+1:n+2]
        if a1 in DDQ:   #要确保实在list里面，否则，极易报错
            rrr = DDQ[a1]
            print(rrr)
            DDDD.append(rrr)
        else:
            rrr = a1
            print(rrr)
            DDDD.append(rrr)
    for n2 in range(len(LL)):
        str = str + DDDD[n2]
    print(DDDD)
    print(str)
    return







LL = 'adam'
LL1 = (LL[1:2])
print(LL1)
print(len(LL))
D1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}
print(D1[LL1])

str2asc('cMBa')

#ADF = int(a)
#print(ADF)

#测试filter函数功能
def is_odd(n):
    return n % 2 == 1 #这里出现过一个问题，=是赋值，而==是布尔比较运算


print(list(filter(is_odd, [1, 2, 4, 5, 6, 7, 8, 9])))  #filter是Iterator, 返回的是惰性序列，需要用list
                                                       #来强制获取所有结果

#测试了lambda功能.strip是删除字符串首尾的空格。
#str.strip('abc'),表明，只要str的首部字符在'abc'中，就会一直删减，直到第一个不在'abc'中停止。尾部字符删减规则也一样。
print(list(filter(lambda s: s and s.strip(), ['A', '', 'B', None, 'C', '   '] )))

#filter求素数
#计算素数可以用埃式筛法
def _odd_iter():  #定义基数生成序列算法
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):    #定义筛选函数
    return lambda x: x % n > 0

def primes():   #定义素数生成序列
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it) #构造新序列

for n in primes():  #由于primes()是一个无限序列，所以调用时需要设置一个退出循环的条件
    if n < 1000:
        print(n)
    else:
        break

#bubble sort(冒泡排序)试验
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
ddq = bubble_sort([45, 36, 58, 12, 25, 68])   #函数对象可以赋值给变量ddq
print(ddq)
print(bubble_sort.__name__)

print(sorted([36, 5, -12, 9, -21]))
print(sorted(['bob', 'ADv', 'cc', 'Ef', 'gd'], key=str.lower, reverse=True)) #按照lower()函数对list进行reverse排序

#试验偏函数的作用：functools.partial
import functools
int2 = functools.partial(int, base=2) #把int函数的base参数值固定为2, 有些地方等同于设定默认参数，减少工作量
print(int2('10010'))


#PYTHON的标准写法
# -*- coding: utf-8 -*-
'a test module'  #程序注释
__author__ = 'Kevin'  #作者姓名

#试验定义Class类的功能
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score



bart = Student('Microsoft', 98)
print('%s, %d' % (bart.name, bart.score))


#貌似可以在class的外部，再对实例添加类的属性，譬如这个grade
bart.grade = '优'
bart.ttt = 987
print(bart.ttt)
print(bart.grade)

#试验不让内部属性被外部访问
class Student_1(object):
    def __init__(self, name, score):
        #属性名称前加上两个下划线__，该变量成为私有变量，只有内部可以访问，外部不可以访问。

        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    #通过定义方法来读取属性，可以对参数做检查，避免无效输入
    def get_name(self):
        return self.__name
    def get_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            print('bad score')


bartt = Student_1('KB', 70)

#私有变量情况下，可以通过函数来获取变量值
print(bartt.get_name())

#看看继承和多态
#Stu1继承Student_1
class Stu1(Student_1):
    pass

class Stu2(Student_1):
    pass

Stu1 = Stu1('KD', 32)
print(Stu1.get_name())

#多态的意义在于：
#继承父类，实现“开闭”原则：对外允许新增子类；而对方法实现式封闭的，不需要进行代码变动

def run_twice(animal):
    animal.run()
    animal.run()

#上面这个定义函数涉及到动态语言(Python)的"file-like object"：鸭子类型。即，一个对象
#只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子

print(isinstance('a', str))
print(dir('a'))
print('a'.lower())
print('a'.__len__())

#关于区分实例属性和类属性
class Student(object):
    name = 'student'
    #__slots__用于限制外部绑定的属性名称，只允许在对应的tuple内
    __slots__ = ('score', 'age', 'time')


s = Student()
print('%s, %s' % (s.name, Student.name))
#s.name = 'Ckp'
print('%s, %s' % (s.name, Student.name))


#这里试验的是动态给class在外部绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score

s = Student()
s1 = Student()

s1.set_score(100)
print(s1.score)

s1.age = 'kw'
s1.time = 'f'


class Student_2(object):
    def __init__(self, name):
        self.name = name
    #__str__方法可以返回一个让用户看到的字符串，可以优化整理输出格式
    def __str__(self):
        return 'Student object (name: %s)' % self.name

print(Student_2('Michael'))


#__iter__ 加上 __next__，
#加上for循环，共同实现一个类的斐波那契数列的迭代
class Fib1(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a
for n in Fib1():
        print(n)

def fib_1(max):
    n, a, b = 0, 1, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'
for n in fib_1(10):
    print(n)


def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

#try...except...finally函数，构成了PYTHON的错误处理机制
#try执行代码，如果出错，则停止执行，跳转至错误处理代码except语句处
#finally语句如果有，就执行，然后结束
def main():
    try:
        bar(0)
    except Exception as e:
        #raise表示抛出错误
        raise ValueError('invalid value: ' )
        #print('Error:', e)
    finally:
        print('finally...')

def foo1(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
def main1():
    foo1('2')

main1()

#这里是为了测试logging作为错误记录的日志文件的功能
#logging.DEBUG表示记录调试相关的信息
#此外，还有logging.INFO,logging.WARNING等信息级别
import logging
logging.basicConfig(level=logging.DEBUG)
s = '2'
n = int(s)
logging.debug('n = %d' % n)
print(10 / n)


#单元测试：可用于测试每一个类
import unittest
class Dict(object):
    def __init__(self, value):
        self.value = value
    def guess1(self, value1, n):
        try:
            value1 = self.value / n
            print('value1 is %d' % value1)
        except Exception as e:
            raise ValueError('value error:')
class TestDict(unittest.TestCase):
    def test_guess1(self):
        d = Dict()
        d.guess1(6, n)
        self.assertTrue(n, 0)


cc = Dict(6)
dd = TestDict()

cc.guess1(6, 1)

#读取文件、图片用到的命令示范
#with open('d:\不得不看的经验.txt', 'r') as f:
   # print(f.read())
#f1 = open('/users/kevin/test.jpg', 'rb')
#f1 = open('/users/kevin/gbk.txt', encoding='gbk', errors='ignore')

#内存中读写，StringIO
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
g = f.getvalue()
print(g)

ff = StringIO('Hello!\nHi !\nGoodbye!')
while True:
    s = ff.readline()
    if s == '':
        break
    print(s.strip())

import os
print(os.name)
print(os.path.abspath('.'))
#这里要注意到\的转义符，如果要表示'\'，要用'\\'表示
print(os.path.join('D:\\', 'testdir'))
#print(os.mkdir('D:\\testdir'))
#os.rmdir('D:\\testdir')

#列出路径下所有的文件
print(os.listdir('.'))
#列出路径下所有的文件夹
print([x for x in os.listdir('.') if os.path.isdir(x)])
#列出路径下所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


#程序运行过程中，所有的数据其实都是在内存中，以下指令试验如何将内存中的数据写到磁盘中
import pickle

import os

#新建一个文件
e = open('d:\\ttt.txt', 'a')
e.write('hello , the world!\n')
e.write('i m back')

