"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/8/9 16:30
"""
import time, random

from lib import Common
from pprint import pprint
import os
import re
from config import const

index_urls = [
    "https://www.sayweee.com/coupons/",
    "http://www.i-funbox.com/coupons/",
    "https://www.extrabux.com/coupons/",
    "https://www.icopyexpert.com/promo-code/",
    "https://www.couponcodealert.com/",
    "https://www.smarterpicks.com/",
    "http://www.idealdvdcopy.com/coupon-codes/",
    "https://www.geoipview.com/coupon-codes/",
]


def screen(browser):
    file_path = const.PUBLIC_ROOT + "index/" + Common.parseUrl(browser.current_url).netloc.replace('www.', '') + ".png"
    browser.get_screenshot_as_file(file_path)
    print('save to {}'.format(file_path))
    browser.quit()


def analyseLinkRDHistory(url):
    print('\nlink redirect history, {}'.format(url))
    import requests
    headers = {'Accept': '*/*', 'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
               'Referer': url}
    try:
        r = requests.get(url, headers=headers, allow_redirects=True, timeout=20)
        # pprint(r.history)
        for a_history in r.history:
            pprint(a_history.url)
    except:
        print('get {} faild'.format(url))
        return


def parserOneCoupon(node):
    title = node.select('.title')[0].text
    link = node.select('.go_crd')[0].get('href')
    coupon_id = node.select('.go_crd')[0].get('data-cid')
    merchant_logo = node.select('img')[0].get('src')
    merchant_name = node.select('img')[0].get('alt')
    return {'title': title, 'coupon_id': coupon_id, 'link': link, 'merchant_name': merchant_name,
            'merchant_logo': merchant_logo}


def analyseCoupon(browser):
    print(browser.current_url)
    purl = Common.parseUrl(browser.current_url)
    domain = purl.scheme + "://" + purl.netloc
    html = browser.page_source
    soup = Common.getBeautifulSoup(html)
    if not soup:
        print('html parser failed')
        return
    coupons = soup.select('.coupon_wrapper')
    print('index页共有{}条促销'.format(len(coupons)))

    # 获取所有的促销详细信息
    coupons_analyse = []
    for coupon in coupons:
        coupon_data = parserOneCoupon(coupon)
        coupons_analyse.append(coupon_data)

    # 随机取一条促销
    a_coupon = random.sample(coupons_analyse, 1)
    if a_coupon['link']:
        if a_coupon['link'].find('http') is -1:
            analyseLinkRDHistory(domain + a_coupon['link'])
        else:
            analyseLinkRDHistory(a_coupon['link'])


def handle(url):
    browser = Common.getSeleniumBrowser(url, no_display=False)
    print('start screen')
    screen(browser)

    analyseCoupon(browser)

    browser.quit()


def init():
    for index_url in index_urls:
        print('\nstart {}'.format(index_url))
        handle(index_url)


if __name__ == '__main__':
    init()
