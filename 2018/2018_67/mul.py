"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/6/4 19:10
"""

import os
from multiprocessing import Process
from time import sleep

# 子进程要执行的代码
def run_proc(name):
    sleep(30)
    print('Child process %s (%s) Running...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print('Process will start.')
        p.start()
        p.join()
    print('Process end.')
