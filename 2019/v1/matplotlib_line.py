#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu-PC
# Software: PyCharm
# Time: 2019-03-18 23:00
# Description: todo list

import matplotlib.pyplot as plt


def init():
    plt.style.use('ggplot')
    revs = [4349.16, 4500.41, 3900.77, 3845.93, 4377.73, 4236.13, 5413.45, 5580.16, 5177.53, 4900.44, 4207.11, 5322.8,
            5307.18, 4514.32, 4050.41, 4853.41, 4633.18, 3408.84, 3892.69, 5280.51, 4245.39, 4462.65, 4603.04, 3762.82,
            4308.38, 3521.65, 5226.19, 5554.05, 4561.49, 5282.42, 4454.06, 4546.0, 4920.52, 5557.86, 6113.09, 4960.01,
            4280.7, 4118.01, 4526.47, 3362.48, 4443.93, 3897.3, 3717.41, 4254.71, 3202.79, 4126.64, 3330.59, 3213.61,
            4330.3, 4181.87, 4018.79, 3745.2, 3637.1, 3811.88, 4494.56, 3699.73, 4134.98, 4503.42, 3655.02, 4291.86,
            4302.71, 4007.94, 3982.34, 5129.96, 4766.02, 4533.44, 4636.82, 4054.47, 4384.51, 4245.43, 2910.64, 4154.11,
            3388.73, 4088.12, 4531.47, 4787.94, 3030.23, 2125.62, 2120.63, 3021.29, 3022.34, 4260.97, 4170.7, 4768.54,
            5455.0, 6057.2, 4679.38, 5327.95, 5393.0, 5560.75, 5660.22, 5522.94, 4723.45, 4261.07]
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(revs, marker=r'o', color=u'blue', linestyle='-', label='Blue Solid')
    ax1.xaxis.set_ticks_position('bottom')
    ax1.yaxis.set_ticks_position('left')
    plt.xlabel('Day')
    plt.ylabel('Revenue')
    plt.title('IFB Revenue Daily')
    plt.legend(loc='best')
    plt.savefig('ifb_rev_line.png', dpi=400, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    init()
