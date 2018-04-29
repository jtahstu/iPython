"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/4/13 15:31
"""

# -*- coding: utf-8 -*-
import random
import scrapy
import time
from pprint import pprint
from DoubanBook.items import CommentItem
from scrapy.exceptions import CloseSpider


class Comment(scrapy.Spider):
    # spider的名字定义了Scrapy如何定位(并初始化)
    # spider，所以其必须是唯一的。 不过您可以生成多个相同的spider实例(instance)，这没有任何限制。 name是spider最重要的属性，而且是必须的
    name = 'comment'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/']
    book_ids = []
    start_book_id = 0
    start_page_id = 1
    max_crawl_page = 2

    def __init__(self, book_ids):
        self.book_ids = book_ids.split(',')

    def start_requests(self):
        return [self.next_request()]

    def parseComment(self, response):
        print("request -> " + response.url)
        comments = response.css('li.comment-item')
        for comment in comments:
            item = CommentItem()
            try:
                item['book_id'] = self.book_ids[self.start_book_id]
                item['comment_id'] = int(comment.css('span.comment-vote>a::attr(data-cid)').extract_first().strip())
                item['user_name'] = comment.css('span.comment-info > a::text').extract_first().strip()
                item['user_home_url'] = comment.css('span.comment-info > a::attr(href)').extract_first().strip()
                item['comment'] = comment.css('p.comment-content::text').extract_first().strip()
                item['vote_count'] = comment.css('span.vote-count::text').extract_first().strip()
                if comment.css('span.user-stars'):
                    item['rating'] = comment.css('span.user-stars::attr(class)').extract_first().strip()
                    item['rating'] = int(item['rating'].split()[1].replace('allstar', '')) / 10
                    item['rating_date'] = comment.css('span.comment-info > span')[1].css(
                        '::text').extract_first().strip()
                else:
                    item['rating_date'] = comment.css('span.comment-info > span::text').extract_first().strip()
                item['updated_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            except Exception as e:
                print(e)
                time.sleep(int(random.uniform(2, 4)))
                continue

            yield item

        self.start_page_id += 1
        if (self.start_page_id > self.max_crawl_page):
            self.start_page_id = 1
            self.start_book_id += 1
            if self.start_book_id >= len(self.book_ids):
                raise CloseSpider('close it')
        time.sleep(int(random.uniform(20, 30)))
        yield self.next_request()

    def next_request(self):
        comment_url = 'https://book.douban.com/subject/{}/comments/hot?p={}'.format(self.book_ids[self.start_book_id],
                                                                                    self.start_page_id)
        return scrapy.http.FormRequest(
            url=comment_url,
            callback=self.parseComment
        )
