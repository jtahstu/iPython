"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/8/10 16:40
"""

import matplotlib.pyplot as plt


def init():
    ifb_revs = [1713.8, 1768.23, 1614.26, 1548.59, 1439.46, 1743.91, 1802.83, 2562.48, 1903.23, 1902.02, 1501.73,
                1629.37, 2222.22, 2074.42, 2338.81, 2361.2, 2324.6, 1805.13, 1536.25, 1385.07, 1957.91, 2000.04, 2853.5,
                2320.1, 2013.53, 1557.46, 2861.75, 2544.34, 1866.85, 2064.67, 2568.58, 2052.42, 1945.81, 2367.98,
                2402.39, 2775.18, 2911.56, 2625.92, 2550.36, 1686.46, 1581.61, 2681.47, 2381.13, 1915.94, 2337.09,
                1667.41, 1681.54, 1751.92, 2076.7, 2715.78, 2085.58, 1439.46, 1514.69, 2034.68, 1854.99, 2359.27,
                2834.09, 1985.02, 2604.92, 1923.06, 1582.07, 2320.34, 2292.76, 2090.42, 2099.15, 2121.83, 1992.38,
                1647.76, 1968.85, 2110.64, 1907.8, 2991.87, 2503.09, 2218.56, 1518.25, 1903.86, 2033.4, 2663.89,
                2146.43, 2427.6, 1978.66, 1667.19, 2205.61, 2607.76, 2756.5, 2943.01, 2849.68, 2435.11, 2474.25,
                2326.16, 2531.14, 3553.9, 3158.03, 2898.54, 3486.01, 2367.83, 3766.92, 3446.09, 3978.09, 2571.85]
    x = [i * 2 for i in range(0, len(ifb_revs))]
    # plt.plot(x,ifb_revs, linewidth=1, ls='-',marker='o', markersize=2)
    # plt.scatter(x, ifb_revs, s=5)
    # plt.figure(figsize=(12,8))
    # plt.show()
    fig, ax = plt.subplots()
    ax.plot(x, ifb_revs)

    ax.grid(True, linestyle='-.')
    ax.tick_params(labelcolor='r', labelsize='medium', width=3)

    plt.show()

if __name__ == "__main__":
    init()