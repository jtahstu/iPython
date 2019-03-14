#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu-PC
# Software: PyCharm
# Time: 2019-03-14 21:52
# Description: todo list


import pandas as pd
import sys


def init():
    file = "../../Data/excel/cr_rev.xlsx"
    file_out = "../../Data/excel/cr_rev_copy.xls"

    header_list = ['xx', 'yy', 'zz']
    # data_frame = pd.read_excel(file, sheet_name='cr_rev', index_col=None, header=None, names=header_list)  加表格头

    data_frame = pd.read_excel(file, sheet_name='cr_rev', index_col=None)
    # i = data_frame.loc[:, ['Date', 'Total Revenue']]
    # print(i)
    data_frame_ifb = data_frame[data_frame['Site'] == 'IFB']

    writer = pd.ExcelWriter(file_out)
    data_frame.to_excel(writer, sheet_name='cr_rev_copy', index=False)
    data_frame_ifb.to_excel(writer, sheet_name='cr_rev_ifb', index=False)

    writer.save()


if __name__ == '__main__':
    init()
