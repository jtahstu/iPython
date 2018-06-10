"""
@author: jtusta
@license: MIT Licence 
@contact: root@jtahstu.com
@site: www.jtahstu.com
@software: PyCharm Community Edition
@file: dfs.py
@time: 2017/01/16 22:17
全排列
"""

a = [0] * 15
b = [0] * 15
n = 0


def dfs(step):
    if step == n + 1:
        print (a[1:n + 1])
    for i in range (1, n + 1):
        if b[i] == 0:
            a[step] = i
            b[i] = 1
            dfs (step + 1)
            b[i] = 0
    return


n = int (input ("请输入n: "))
dfs (1)

import itertools
for i in itertools.permutations(range(3),3):
    print(i)