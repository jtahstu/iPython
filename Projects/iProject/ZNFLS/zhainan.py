import json
import random
import time
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import pymysql
import pymysql.cursors
import re
import urllib.request
import os

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='spider',
                             port=3306,
                             charset='utf8')
cursor = connection.cursor()


def write(path, links):
    print('links has {} lines'.format(len(links)))
    with open(path, 'w') as w:
        w.write(links)


def read(path):
    with open(path, 'r') as r:
        return r.read()


def getDateTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def query(sql):
    cursor.execute(sql)
    res = cursor.fetchall()
    connection.commit()
    return res


def getHtml(url):
    print('request url {}'.format(url))
    # salt = ''.join(random.sample(string.ascii_letters + string.digits, 11))
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'Hm_lvt_178790a0284fb8d2862083c6d96e5d22=1524932666,1525116718; Hm_lpvt_178790a0284fb8d2862083c6d96e5d22=1525116718; tin_check_nonce=32a8175dfb',
        'upgrade-insecure-requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    try:
        html = requests.get(url, headers=headers, timeout=10)
    except:
        time.sleep(5)
        getHtml(url)  # 递归
    if html.status_code != 200:
        sleep_sec = random.randrange(6, 12)
        print('status_code is %d , error msg is %s , random wait %ds' % (html.status_code, html.text, sleep_sec))
        time.sleep(sleep_sec)
        getHtml(url)  # 递归
    time.sleep(random.randrange(1, 3))
    return html.text


def getLinks(url='https://www.zhainanfulishe.net/nvshen'):
    html = getHtml(url)
    if not len(html):
        return 'die {}'.format(url)
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('article.home-blog-entry')
    links = []
    for item in items:
        link = item.a.get("href")
        if link.index('https') == 0:
            links.append(link)
    return links


# 宅男女神列表
def getNSlists():
    lists = getLinks('https://www.zhainanfulishe.net/nvshen')
    for i in range(2, 50):
        url = 'https://www.zhainanfulishe.net/nvshen/page/{}'.format(i)
        list = getLinks(url)
        if list:
            lists.append(list)
        elif len(list) != 10:
            write('./znns_link2.json', json.dumps(lists))
            break
    write('./znns_link_bak.json', json.dumps(lists))


def getDetail(url):
    html = getHtml(url)
    if not len(html):
        return 'die {}'.format(url)
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('div#breadcrumbs')[0].h1.text.strip()
    date = soup.select('span.single-meta-time')[0].text.strip()
    content = soup.select('div.single-text')[0].text.strip()
    pics = soup.select('div.single-text img')
    pic_hrefs = []
    for pic in pics:
        pic_href = pic.get('src')
        if pic_href:
            pic_hrefs.append(pic_href)
    print('title {}\ndate {}\ncontent len {}\nimg count {}\n'.format(title, date, len(content), len(pics)))
    return (connection.escape(title), date, connection.escape(content), json.dumps(pic_hrefs))


# 宅男女神详情页
# CREATE TABLE `znfls_znns` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `aid` int(11) DEFAULT NULL,
#   `url` varchar(64) DEFAULT NULL,
#   `title` varchar(256) DEFAULT NULL,
#   `content` text,
#   `date` varchar(32) DEFAULT NULL,
#   `pics` text,
#   `add_time` datetime DEFAULT NULL,
#   `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=487 DEFAULT CHARSET=utf8
def getNSDetail():
    links = read('./znns_link_bak.json')
    links = json.loads(links)
    for link in links[111:]:
        aid = re.sub(r'\D', '', link)  # 拿到链接中的数字
        title, date, content, pics = getDetail(link)
        sql = "INSERT INTO `znfls_znns`(`aid`,`url`,`title`,`content`,`date`,`pics`,`add_time`) VALUES({},'{}',{},{},'{}','{}','{}')".format(
            aid, link, title, content, date, pics, getDateTime()
        )
        query(sql)


# 宅男频道列表
def getPDList():
    lists = getLinks('https://www.zhainanfulishe.net/znpd')
    for i in range(2, 56):
        url = 'https://www.zhainanfulishe.net/znpd/page/{}'.format(i)
        list = getLinks(url)
        if list:
            lists.append(list)
        elif len(list) != 10:
            write('./znpd_link.json', json.dumps(lists))
            break
    write('./znpd_link_bak.json', json.dumps(lists))


# 宅男频道，数据库同宅男女神表，分了下表
def getPDDetail():
    links = read('./znpd_link_bak.json')
    links = json.loads(links)
    for link in links[532:]:
        aid = re.sub(r'\D', '', link)  # 拿到链接中的数字
        title, date, content, pics = getDetail(link)
        sql = "INSERT INTO `znfls_znpd`(`aid`,`url`,`title`,`content`,`date`,`pics`,`add_time`) VALUES({},'{}',{},{},'{}','{}','{}')".format(
            aid, link, title, content, date, pics, getDateTime()
        )
        query(sql)


def downPic(url, path, path2=''):
    print('get from {}, save to {}'.format(url, path))
    time.sleep(random.randrange(1, 3))
    try:
        content = urllib.request.urlopen(url, timeout=10).read()
    except:
        return
    with open(path, 'wb') as w:
        w.write(content)
    if path2:
        with open(path2, 'wb') as w2:
            w2.write(content)


def downPDPics():
    sql = 'SELECT * FROM `znfls_znpd` WHERE title not like "%里番%"'
    items = query(sql)
    for item in items[1:]:
        _, aid, _, title, _, _, pics, _, _ = item
        if aid > 603:
            continue
        print('start aid {}'.format(aid))
        pics = json.loads(pics)
        pic_dir = 'D:/Code/iPython/Projects/spider/ZNPD/{}-{}/'.format(aid, title)
        if not os.path.isdir(pic_dir) and not os.path.exists(pic_dir):
            try:
                os.mkdir(pic_dir)
            except:
                pic_dir = 'D:/Code/iPython/Projects/spider/ZNPD/{}/'.format(aid)
                os.mkdir(pic_dir)
        for pic in pics:
            path = pic_dir + os.path.basename(pic)
            path2 = 'D:/Code/iPython/Projects/spider/ZNPD_ALL/' + '{}_{}'.format(aid, os.path.basename(pic))
            downPic(pic, path, path2)


from selenium import webdriver

browser = webdriver.Firefox()
driver = webdriver.PhantomJS()
driver.set_page_load_timeout(3)
driver.maximize_window()  # 设置全屏
driver.set_window_size('1366', '768')


def downFullScreen():
    sql = "SELECT url FROM `znfls_znpd` WHERE title NOT LIKE '%里番%'"
    urls = query(sql)
    for url in urls:
        url = str(url[0])
        path = './ZNPD_SCREEN/' + re.sub(r'\D', '', url) + '.png'
        print("get {} save to {}".format(url, path))
        try:
            driver.get(url)
            driver.save_screenshot(path)
        except Exception as e:
            print(e)


downFullScreen()
cursor.close()
connection.close()
driver.close()
browser.close()
