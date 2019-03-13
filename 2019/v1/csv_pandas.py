#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu-PC
# Software: PyCharm
# Time: 2019-03-13 22:08
# Description: todo list

import pandas, glob, os
from pprint import pprint


def init():
    file = "../../Data/csv/cr_rev.csv"
    out_file = "../../Data/csv/cr_rev_search.csv"
    out_file_json = "../../Data/csv/cr_rev_search.json"
    data_frame = pandas.read_csv(file)
    data_frame['Total Revenue'] = data_frame['Total Revenue'].str.replace(',', '').astype(float)
    l = data_frame.loc[data_frame['Total Revenue'] > 5000, :]
    # pprint(l)
    # l.to_csv(out_file, index=False)
    # l.to_json(out_file_json)

    i = data_frame.loc[:, ['Date', 'Total Revenue']]
    # print(i)

    # print(data_frame.loc[data_frame['Site'] == 'IFB', 'Total Revenue'])
    # exit(-1)
    sum = pandas.DataFrame(float(str(v).replace(',', '')) for v in data_frame.loc[data_frame['Site'] == 'IFB', 'Total Revenue']).sum()
    print(sum)
    avg = pandas.DataFrame(float(str(v).replace(',', '')) for v in data_frame.loc[data_frame['Site'] == 'IFB', 'Total Revenue']).mean()
    print(avg)

def glob_test():
    path = '..\..\Data\csv'
    print(os.path.join(path, '*.csv'))
    print(glob.glob(os.path.join(path, '*.csv')))


if __name__ == '__main__':
    init()
    # glob_test()
