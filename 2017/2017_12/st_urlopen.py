"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@software: PyCharm
@time: 2017/12/5 10:23
"""

import json
from urllib.request import urlopen


# url = "http://i.jtup.cc/book/php"
# response = urlopen(url)
# contents = response.read()
# text = contents.decode('utf8')

text = urlopen('http://i.jtup.cc/book/ph').read().decode('utf8')
data = json.loads(text)

for video in data:
    print(video['title'][0:3])
