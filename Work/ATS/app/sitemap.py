"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/7/15 01:36
"""
import time, sys
sys.path.append('/Users/jtusta/PycharmProjects/iPython/Work/ATS')

from lib import Common
from pprint import pprint
import os
import re
from config import const

sitemap_urls = [
    "https://sayweee.com/coupons/sitemapm05.xml",
    "http://www.i-funbox.com/coupons/sitemapm07.xml",
    "https://www.extrabux.com/coupons/sitemapm09.xml",
    "https://www.icopyexpert.com/promo-code/sitemapm11.xml",
    "https://www.couponcodealert.com/sitemapm12.xml",
    "https://www.smarterpicks.com/sitemapm13.xml",
    "http://www.idealdvdcopy.com/coupon-codes/sitemapm14.xml",
    "https://www.geoipview.com/coupon-codes/sitemapm15.xml",
]


def handle(url):
    print("start {}, {}".format(url, Common.getDateTime()))
    r = Common.getRequestsHtml(url)

    filename = os.path.basename(url).replace('.', '_' + Common.getHour() + '.')
    file_save_path = "{}{}/{}".format(const.SITEMAP_ROOT, Common.getDate(), filename)

    if not os.path.exists(os.path.dirname(file_save_path)):
        os.mkdir(os.path.dirname(file_save_path))

    with open(file_save_path, 'w', encoding='utf-8') as w:
        w.write(r.html.html)

    locs = re.findall(r"<loc>(.*?)</loc>", str(r.html.html))
    last_mods = re.findall(r"<lastmod>(.*?)</lastmod>", str(r.html.html))

    # 检查文件更新时间
    update_date = last_mods[0]
    for last_mod in last_mods:
        if update_date != last_mod:
            print(r.html.html)
            print('error: xml文件更新时间竟然不一样')
            return

    now_date = Common.getDate()
    now_sec = time.mktime(time.strptime(now_date, '%Y-%m-%d'))
    update_sec = time.mktime(time.strptime(update_date, '%Y-%m-%d'))
    sub_days = int((now_sec - update_sec) / (24 * 60 * 60))
    if (sub_days >= 2):
        print(r.html.html)
        print('error: xml文件更新时间与当前时间差别较大')
        return

    pprint(locs)
    pprint(last_mods)
    print("i think it's ok")
    print("end {}, {}\n\n".format(url, Common.getDateTime()))


def init():
    for sitemap_url in sitemap_urls:
        handle(sitemap_url)


if __name__ == '__main__':
    init()
