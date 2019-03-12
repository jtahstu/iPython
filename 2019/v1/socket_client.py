#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Software: PyCharm
# Time: 2018-12-27 17:20
# Description: todo list

import socket


def init():
    s = socket.socket()
    host = socket.gethostname()
    s.connect((host, 1234))
    print(s.recv(1024))


if __name__ == '__main__':
    init()
