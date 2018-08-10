"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/7/15 01:09
"""
import requests
from bs4 import BeautifulSoup

from config import const_common
from lib import iMySQL
from lib import iMongo
from lib import Common

imysql = iMySQL
imongo = iMongo

import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PUBLIC_ROOT = PROJECT_ROOT + "/public/"
SITEMAP_ROOT = PROJECT_ROOT + "/public/sitemap/"
