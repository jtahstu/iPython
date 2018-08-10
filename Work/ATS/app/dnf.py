"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/8/10 14:39
"""
from lib import Common
from pprint import pprint
from urllib.parse import urlparse

arad_url = 'http://dnf.gamebbs.qq.com/forum-42-1.html'
domain = 'http://dnf.gamebbs.qq.com/'


def getDetail(bbs):
    url = bbs['href']
    html = Common.getHtml(url)
    soup = Common.getBeautifulSoup(html.text)
    lis = soup.select('.t_f')
    if len(lis) == 0:
        return
    lis = [li.text for li in lis]
    pprint(lis)

    url = Common.parseUrl(url)
    tid = [item for item in url.query.split('&') if item.find('tid=') is 0]
    tid = tid[0].replace('tid=', '')
    pprint(tid)


def init():
    html = Common.getHtml(arad_url)
    soup = Common.getBeautifulSoup(html.text)
    lis = soup.select('.frmc')
    bbses = []
    for li in lis:
        if len(li.select('.frmc_t > a')) > 0:
            a = li.select('.frmc_t > a')[0]
            title = a.text or ''
            href = domain + a.get('href') or ''
        if len(li.select('span[title]')) > 0:
            date = li.select('span[title]')[0].get('title') or ''
        print(title, href, date)
        bbs = {'title': title, 'href': href, 'date': date}
        bbses.append(bbs)
        getDetail(bbs)


if __name__ == "__main__":
    init()
