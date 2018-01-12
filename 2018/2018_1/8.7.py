"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2018/1/10 15:09
"""
# 1
from pprint import pprint

test1 = 'This is a test of the emergency text system'
testw = open('test.txt', 'wt')
testw.write(test1)
testw.close()
# 2
with open('test.txt', 'rt') as testr:
    test2 = testr.read()
print(test2 == test1)  # True
# 3
bookstr = """author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
"""
with open('books.csv', 'wt') as testc:
    testc.write(bookstr)
# 4 第二本书引号没了，但是逗号没有被分割
import csv

with open('books.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]
print(books)
# 5 名字为 book2.csv
# 6
import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()
# curs.execute('''CREATE TABLE books
# (title TEXT,
# author TEXT,
# year INT)''')

# 7 原字符串中含有é，导致读出的时候显示编码错误，就替换掉了
bookstr2 = """title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Mieville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
"""
with open('books2.csv', 'wt') as testc2:
    testc2.write(bookstr2)

sql = "insert into books(title,author,year) values (?,?,?)"
with open('books2.csv', 'rt') as cb:
    dicts = csv.reader(cb)
    books2 = [row for row in dicts]
print(books2[1:])
for d in books2[1:]:
    res = curs.execute(sql, (d[0], d[1], int(d[2])))
    print(res)
conn.commit()  # 这里 commit一下可以把数据写入到文件，不然数据就只存在与内存中
# 8
curs.execute('SELECT title FROM books ORDER BY title')
rows = curs.fetchall()
pprint(rows)  # 为什么这里多了个逗号，不太清楚
# 9
curs.execute('SELECT * FROM books ORDER BY year')
rows2 = curs.fetchall()
pprint(rows2)
curs.close()
conn.close()

# 以下三个问题都没测试，因为模块没装，但感觉问题不大
# 10
import sqlalchemy as sa

conn2 = sa.create_engine('sqlite://')
rows3 = conn.execute('SELECT title FROM books ORDER BY title')
for row in rows3:
    print(row)

# 11
import redis

conn3 = redis.Redis()
conn3.hset('test', {'count': 1, 'name': 'Fester Bestertester'})
print(conn.hget('test'))

# 12
conn3.hincr('test', 'count')
