#这里讲到了多进程：即打开的多个应用程序，包括操作系统隐藏的程序操作；Process
#多线程：某一个应用程序，可能要涉及到复制、粘贴、删除等操作，是一个进程里面的多个子任务；Thread
import os
from multiprocessing import Process

def run_proc(name):
    print('Run child process %s %s...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
#    p = Process(target=run_proc, args=('test',))
 #   print('child process will start')
  #  p.start()
   # print('child process end')

#正则表达式的字符串匹配功能很强大，测试如下功能：
import re
if re.match(r'^\d{3}\-\d{3,8}$', '010-1235'):
    print('ok')
else:
    print('failed')

#切分字符串
f = 'a b   c'
#常规分割字符串方法
print(f.split(' '))
#用re的字符串分割
print(re.split(r'\s+', f))
#用[]表示范围匹配，类似于多项式匹配
print(re.split(r'[\s\,]+', 'a,b,c   d'))

#正则表达式的分组功能
#通过()来实现分组功能，然后用group()实现提取子串功能
m = re.match(r'(\d{3})-(\d{3,8})$', '010-12356')
print(m)
print(m.group(1))

print(re.match(r'^(\d+?)(1*)$', '1023111').groups())


#关于日期的相关函数的用法
from datetime import datetime
#当前时间
print(datetime.now())
#当前时间相对于epoch time的秒数
print(datetime.timestamp(datetime.now()))
#返回当前时间
print(datetime.fromtimestamp(1559999999))
#返回当前utc时间
print(datetime.utcfromtimestamp(1559999999))


#将用户输入的字符串形式的日期、时间，转换为datetime
cday = datetime.strptime('2019-6-6 13:27', '%Y-%m-%d %H:%M')
print(cday)

#将用户输入的datetime形式的日期、时间，转换为string
cday1 = datetime(2019, 6, 6, 13, 31)
print(cday1.strftime('%A, %b %d %H:%M'))

#对datetime进行加减运算，通过delta
from datetime import datetime, timedelta
print(datetime.now() + timedelta(hours=10))

print(datetime.now() - timedelta(days=1))

from datetime import timezone
#关于如何设置utc时间
utc_dt2 = datetime.now()
print(utc_dt2)
utc_dt1 = datetime.utcnow()
print(utc_dt1)
#utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
#print(utc_dt)

#实现各时区内UTC时间的转化，譬如北京时间，东京时间
bj_dt = utc_dt2.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

tokyo_dt = utc_dt2.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)






#使用collections模块
#1、namedtuple模块
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
print(Point(1, 2).x)

#2、deque模块,为了更高效的实现插入和删除操作的双向list:
from collections import deque
q = deque([1, 2, 3])
q.popleft()
print(q)

#3、defaultdict是指当引用的key不存在时，返回一个默认值
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key2'])

#4、dict内部的key是无序的，如果要key保持顺序，可以用orderdict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od =OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

#5、计数器counter的用法，譬如统计字符出现次数
from collections import Counter
c = Counter()
for ch in 'djfjjjdjfd':
    c[ch] = c[ch] + 1
print(c)