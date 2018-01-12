"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2018/1/11 13:48
"""

from datetime import datetime, date

# 1 把当前日期以字符串形式写入文本文件today.txt
now = datetime.today()
with open('today.txt', 'wt') as w:
    res = w.write(str(now))
    print(res)
# 2 从today.txt 中读取字符串到today_string 中
with open('today.txt', 'rb') as r:
    today_string = r.readline().decode('utf-8')
    print(today_string)
# 3 从today_string 中解析日期
dateNow = datetime.strptime(today_string, "%Y-%m-%d %H:%M:%S.%f").date()
print(dateNow)
# 4 列出当前目录下的文件
import os

files = [file for file in os.listdir('.') if os.path.isfile(file)]
print(files)
# 5 列出父目录下的文件
filesP = [file for file in os.listdir('../') if os.path.isfile(file)]
print(filesP)
# 6 使用multiprocessing 创建三个进程，让它们等待随机的秒数（范围1~5），打印出当前时间并退出
import multiprocessing
from time import sleep
import random


def p(i):
    sleep(random.randrange(1, 5))
    print('process %d , now is %s' % (i, str(datetime.today())))
    quit(0)


for i in range(3):
    pc = multiprocessing.Process(target=p, args=(i,))
    pc.start()
# 7 用你的生日创建一个date 对象
birthday = date(1995, 10, 29)
# 8 你的生日是星期几？
dayOfWeek = birthday.weekday()
print(dayOfWeek)
# 9 你出生10 000 天的日期是什么？
from datetime import timedelta

birthday1000 = birthday + timedelta(days=1000)
print(birthday1000)

