# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LianjiaItem
#from ..loaders import *


class ErshoufangSpider(CrawlSpider):
    name = 'ershoufang'
    allowed_domains = ['gz.lianjia.com']
    start_urls = ['https://gz.lianjia.com/ershoufang']


    rules = (
        Rule(LinkExtractor(allow='ershoufang\/.*\.html',
                           restrict_xpaths='//div[@class="info clear"]'), callback='parse_item'),
        #Rule(LinkExtractor(allow='https://gz.lianjia.com/ershoufang\/pg\d+\/',
                          # restrict_xpaths='/html/body/div[4]/div[1]/div[8]/div[2]/div/a[5]'))
    )




    def parse_item(self, response):
        for i in range(100):
            next = 'https://gz.lianjia.com/ershoufang/pg{}/'.format(str(i))
            url1 =response.urljoin(next)
            yield scrapy.Request(url=url1)
            item = LianjiaItem()
            # loader = ErShouFangLoader(item=LianjiaItem(), response=response)
            # loader.add_xpath('title','//div[@class="title"]//h1[@class="main"]/text()')
            # loader.add_xpath('community', '//div[@class="communityName"]//a[@class="info "]/text()')
            # loader.add_xpath('model', '//div[@class="room"]//div[@class="mainInfo"]/text()')
            # loader.add_xpath('area', '//div[@class="area"]//div[@class="mainInfo"]/text()')
            # loader.add_xpath('price', '//div[@class="price "]//span[@class="total"]/text()')
            # loader.add_xpath('average_price', '//div[@class="unitPrice"]//span[@class="unitPriceValue"]/text()')
            # loader.add_xpath('url', response.url)
            # loader.add_xpath('city', '//div[@class="areaName"]//a[@target="_blank"]/text()')
            item['title'] = response.xpath('//div[@class="title"]//h1[@class="main"]/text()').extract_first()
            item['community'] = response.xpath('//div[@class="communityName"]//a[@class="info "]/text()').extract_first()
            item['model'] = response.xpath('//div[@class="room"]//div[@class="mainInfo"]/text()').extract_first()
            item['area'] = response.xpath('//div[@class="area"]//div[@class="mainInfo"]/text()').extract_first()
            item['price'] = response.xpath('//div[@class="price "]//span[@class="total"]/text()').extract_first()+"万"
            item['average_price'] = response.xpath('//div[@class="unitPrice"]//span[@class="unitPriceValue"]/text()').extract_first()+\
                                    response.xpath('//div[@class="unitPrice"]//i/text()').extract_first()
            item['url'] = response.url
            item['city'] = response.xpath('//div[@class="areaName"]//a[@target="_blank"]/text()').extract_first()+"区"
            item['focus_num'] = response.xpath('//div[@class="action"]//span[@class="count"]/text()').extract_first()
            yield item





