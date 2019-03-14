#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu-PC
# Software: PyCharm
# Time: 2019-03-14 21:20
# Description: todo list

import sys, datetime
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from pprint import pprint


def init():
    file = "../../Data/excel/cr_rev.xlsx"
    workbook = open_workbook(file)
    print(workbook.nsheets)
    for worksheet in workbook.sheets():
        print("{} {} {}".format(worksheet.name, worksheet.nrows, worksheet.ncols))

        for row in range(worksheet.nrows):
            for col in range(worksheet.ncols):
                value = worksheet.cell_value(row, col)
                if worksheet.cell_type(row, col) == 3:  # 处理下日期格式
                    value = xldate_as_tuple(value, workbook.datemode)
                    # print(value)
                    value = datetime.date(*value[0:3]).strftime('%Y-%m-%d')
                print("{} ".format(value), end='')
            print()
            if (row > 5):
                break


if __name__ == '__main__':
    init()
