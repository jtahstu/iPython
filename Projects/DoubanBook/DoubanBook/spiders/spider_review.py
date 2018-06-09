"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/4/13 17:58
"""

# -*- coding: utf-8 -*-
import random
import scrapy
import time
import json
import requests
from pprint import pprint
from DoubanBook.items import ReviewItem
from scrapy.exceptions import CloseSpider


class Review(scrapy.Spider):
    # spider的名字定义了Scrapy如何定位(并初始化)
    # spider，所以其必须是唯一的。 不过您可以生成多个相同的spider实例(instance)，这没有任何限制。 name是spider最重要的属性，而且是必须的
    name = 'review'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/']
    book_ids = []
    start_book_id = 0
    start_id = 0
    max_crawl_page = 20 - 1

    def __init__(self, book_ids):
        self.book_ids = book_ids.split(',')

    def start_requests(self):
        return [self.next_request()]

    def parse_review(self, response):
        print("request -> " + response.url)
        reviews = response.css('div.review-item')
        for review in reviews:
            item = ReviewItem()
            try:
                item['book_id'] = self.book_ids[self.start_book_id]
                item['review_id'] = int(review.css('::attr(id)').extract_first().strip())
                print("review id is {} \n".format(item['review_id']))
                item['user_name'] = review.css('a.name::text').extract_first().strip()
                item['user_home_url'] = review.css('a.name::attr(href)').extract_first().strip()
                jsons = self.get_review_detail(review_id=item['review_id'])
                item['review'] = jsons['html']
                item['review_body'] = jsons['body']
                item['useful_count'] = jsons['votes']['useful_count']
                item['useless_count'] = jsons['votes']['useless_count']
                item['reply_count'] = int(review.css('a.reply::text').extract_first().strip().replace('回应', ''))
                item['rating'] = review.css('span.main-title-rating::attr(class)').extract_first().strip()
                item['rating'] = int(item['rating'].split()[0].replace('allstar', '')) / 10
                item['rating_time'] = review.css('span.main-meta::text').extract_first().strip()
                item['updated_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            except Exception as e:
                print(e)
                time.sleep(int(random.uniform(2, 4)))
                continue
            yield item

        self.start_id += 20
        if (self.start_id > self.max_crawl_page):
            self.start_id = 0
            self.start_book_id += 1
            if self.start_book_id >= len(self.book_ids):
                raise CloseSpider('close it')
        time.sleep(int(random.uniform(20, 30)))
        yield self.next_request()

    def next_request(self):
        review_url = 'https://book.douban.com/subject/{}/reviews?start={}'.format(self.book_ids[self.start_book_id],
                                                                                  self.start_id)
        return scrapy.http.FormRequest(
            url=review_url,
            callback=self.parse_review
        )

    def get_review_detail(self, review_id):
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Cookie': 'bid=cz4zx3jnczk',
            'DNT': '1',
            'Host': 'book.douban.com',
            'Referer': 'https://book.douban.com/subject/{}/reviews'.format(review_id),
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        full_url = "https://book.douban.com/j/review/{}/full".format(review_id)
        time.sleep(int(random.uniform(5, 10)))
        str = requests.get(url=full_url, headers=headers)
        return json.loads(str.text)
