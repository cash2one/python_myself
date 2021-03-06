# -*- coding: utf-8 -*-
#引入文件
import scrapy
#引入容器
from scrapytest.CourseItems import CourseItem


class MySpider(scrapy.Spider):
    #用于区别Spider
    name = "MySpider"
    #允许访问的域
    allowed_domains = ["imooc.com"]
    #爬取的地址
    start_urls = ["http://www.imooc.com/course/list"]
    #爬取方法
    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = CourseItem()
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 先获取每个课程的div
        for box in response.xpath('//div[@class="moco-course-wrap"]/a[@target="_self"]'):
            # 获取每个div中的课程路径
            item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
            # 获取div中的课程标题
            item['title'] = box.xpath('.//img/@alt').extract()[0].strip()
            # 获取div中的标题图片地址
            item['image_url'] = box.xpath('.//@src').extract()[0]
            # 获取div中的学生人数
            item['student'] = box.xpath('.//span/text()').extract()[0].strip()[:-3]
            # 获取div中的课程简介
            item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
            # 返回信息
            yield item