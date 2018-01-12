"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@software: PyCharm
@time: 2017/8/28 13:49
"""

import requests
import time
import json

api = "http://cnz.co/domain-registration/domain.php?action=caajax&domain_name="
def init():
    for i in range(0,26):
        for j in range(0,26):
            for k in range(0,26):
                try:
                    domain = chr(97+i)+chr(97+j)+chr(97+k)+".cc"
                    print("正在尝试 {} ".format(domain))

                    html = requests.get(api+domain,timeout=3).text
                    status = json.loads(html)
                    if status['status']=="available":
                        print("{} is available ! hahaha")

                except Exception as e:
                    print(e)
                    continue
                # time.sleep(1)


if __name__ == "__main__":
    init()