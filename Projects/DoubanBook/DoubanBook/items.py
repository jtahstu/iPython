# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CommentItem(scrapy.Item):
    book_id = scrapy.Field()
    comment_id = scrapy.Field()
    user_name = scrapy.Field()  # 用户名
    user_home_url = scrapy.Field()  # 用户链接
    comment = scrapy.Field()  # 评论
    vote_count = scrapy.Field()  # 有用数
    rating = scrapy.Field()  # 评分
    rating_date = scrapy.Field()  # 评分日期
    updated_at = scrapy.Field()  # 抓取时间


class ReviewItem(scrapy.Item):
    book_id = scrapy.Field()
    review_id = scrapy.Field()
    user_name = scrapy.Field()  # 用户名
    user_home_url = scrapy.Field()  # 用户链接
    review = scrapy.Field()  # 书评
    review_body = scrapy.Field()  # 书评
    useful_count = scrapy.Field()  # 有用数
    useless_count = scrapy.Field()  # 没用数
    reply_count = scrapy.Field()  # 回应数
    rating = scrapy.Field()  # 评分
    rating_time = scrapy.Field()  # 评分日期
    # publisher = scrapy.Field()  # 出版社
    updated_at = scrapy.Field()  # 抓取时间
