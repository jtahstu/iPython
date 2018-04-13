"""
@author: jtusta
@license: MIT Licence 
@contact: root@jtahstu.com
@site: www.jtahstu.com
@software: PyCharm Community Edition
@file: downPics.py
@time: 2017/01/09 21:35
"""

import urllib.request
import os
import re

url = r'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%8A%A8%E6%BC%AB&oq=%E5%8A%A8%E6%BC%AB&rsp=-1'

imgPath = r'F:\img'

imgHtml = urllib.request.urlopen(url).read().decode('utf-8')
urls = re.findall(r'"objURL":"(.*?)"', imgHtml)

if not os.path.isdir(imgPath):
    os.mkdir(imgPath)

index = 1
for url in urls:
    print("下载:", url)

    # 未能正确获得网页 就进行异常处理
    try:
        res = urllib.request.urlopen(url)

        if str(res.status) != '200':
            print('未下载成功：', url)
            continue
    except Exception as e:
        print('未下载成功：', url)

    filename = os.path.join(imgPath, str(index) + '.jpg')
    with open(filename, 'wb') as f:
        f.write(res.read())
        print('下载完成\n')
        index += 1
print("下载结束，一共下载了 %s 张图片" % (index - 1))