"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/8/9 16:30
"""
import time, random, sys, os, re, time, json

sys.path.append('/Users/jtusta/PycharmProjects/iPython/Work/ATS')

from lib import Common
from pprint import pprint
from config import const
from lib import iImage

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


def screen(url, browser):
    file_path = const.screen_image_path + Common.parseUrl(url).netloc.replace('www.', '')
    browser.get_screenshot_as_file(file_path + "_header.png")
    print('save to {}'.format(file_path))
    js = "document.documentElement.scrollTop=10000"
    browser.execute_script(js)
    browser.get_screenshot_as_file(file_path + "_footer.png")
    browser.quit()


def analyseLinkRDHistory(url):
    print('\nlink redirect history with {}'.format(url))
    import requests
    headers = {'Accept': '*/*', 'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
               'Referer': url}
    try:
        r = requests.get(url, headers=headers, allow_redirects=True, timeout=30)
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


def analyseCoupon(url, browser):
    purl = Common.parseUrl(url)
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
    # 保存所有促销数据
    filename = const.coupon_data_path + Common.parseUrl(url).netloc.replace('www.', '') + '.json'
    with open(filename, 'w') as w:
        w.writelines(json.dumps(coupons_analyse))

    # 随机取一条促销，分析跳出链接
    a_coupon = random.choice(coupons_analyse)
    if a_coupon['link']:
        if a_coupon['link'].find('http') is -1:
            analyseLinkRDHistory(domain + a_coupon['link'])
        else:
            analyseLinkRDHistory(a_coupon['link'])


def handle(url):
    # 截图
    browser = Common.getSeleniumBrowser(url, display=True)
    print('start screen')
    screen(url, browser)
    browser.quit()

    # 分析页面促销
    browser = Common.getSeleniumBrowser(url, display=False)
    analyseCoupon(url, browser)
    browser.quit()


def init():
    Common.clearDir(const.screen_image_path)
    Common.clearDir(const.coupon_data_path)
    for index_url in index_urls:
        print('\nstart {}'.format(index_url))
        try:
            handle(index_url)
        except Exception as e:
            print('{} has Error, msg: {}'.format(index_url, e))
            continue
    # 截图合并
    print('start vertical merger images')
    iImage.verticalMerger(const.screen_image_path, const.screen_all_output)

    # 促销数据合并
    print('start merger index coupon data')
    all_coupon_data = []
    for coupon_file in Common.getSortedDirList(const.coupon_data_path):
        site = coupon_file.split('.')[0]
        with open(const.coupon_data_path + coupon_file, 'r') as r:
            data = json.load(r)
            for (key, item) in enumerate(data):
                data[key].update({'site': site})
            all_coupon_data.append(data)
    with open(const.coupon_data_output, 'w') as w:
        w.writelines(json.dumps(all_coupon_data))


if __name__ == '__main__':
    init()
