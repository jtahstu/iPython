#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu-PC
# Software: PyCharm
# Time: 2019-03-13 22:02
# Description: todo list

import csv

def init():
    file = "../../Data/csv/cr_rev.csv"
    with open(file, 'r', newline='\n') as r:
        reader = csv.reader(r)
        next(reader)
        for row in reader:
            rev = row
            print(rev)
            return


if __name__ == '__main__':
    init()


