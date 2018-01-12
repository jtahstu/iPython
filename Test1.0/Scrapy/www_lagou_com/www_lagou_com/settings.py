# -*- coding: utf-8 -*-

# Scrapy settings for www_lagou_com project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'www_lagou_com'

SPIDER_MODULES = ['www_lagou_com.spiders']
NEWSPIDER_MODULE = 'www_lagou_com.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'www_lagou_com (+http://www.yourdomain.com)'

# Obey robots.txt rules
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
FEED_URI = '/Users/jtusta/PycharmProjects/Python/Test1.0/Scrapy/www_lagou_com/back.csv'
FEED_FORMAT = 'csv'

COOKIES_ENABLED = True

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_NAME = 'iApp'
MONGODB_TABLE = 'jobs_lagou_php'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '23',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'user_trace_token=20171214222435-8245db41-e0da-11e7-9d45-5254005c3644; LGUID=20171214222435-8245de65-e0da-11e7-9d45-5254005c3644; index_location_city=%E4%B8%8A%E6%B5%B7; _ga=GA1.2.566616671.1513261475; JSESSIONID=ABAAABAACEBACDGEA354AFB727F9DD672DAABD269C1A08F; _gid=GA1.2.1337386859.1513581214; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513261476,1513581214; LGSID=20171218151334-f5dbe587-e3c2-11e7-9e48-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_navigation; SEARCH_ID=170f28639d7c4f49a5339dd187dd9e55; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513581333; LGRID=20171218151533-3c79f3d3-e3c3-11e7-9e48-525400f775ce',
    'DNT': '1',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.lagou.com/jobs/list_PHP?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput=',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'www_lagou_com.middlewares.WwwLagouComSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'www_lagou_com.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'www_lagou_com.pipelines.WwwLagouComPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
