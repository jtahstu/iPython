#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Software: PyCharm
# Time: 2018-12-27 17:17
# Description: todo list

import socket


def init():
    s = socket.socket()

    host = socket.gethostname()
    s.bind((host, 1234))

    s.listen(5)
    while True:
        c, addr = s.accept()
        print('get connection from', addr)
        c.send(b'Thank you for connection')
        c.close()


if __name__ == '__main__':
    init()
