# -*- coding: utf-8 -*-
import scrapy
from ShopAround.items import JdItem

class JdSpider(scrapy.Spider):
    start_urls = []
    name = 'jd'
    allowed_domains = ['search.jd.com/']
    search_name = input('你输入想要查询的京东商品名称: ')
    pages = int(input('你输入想要爬取京东的商品页数: '))

    for page in range(1, pages):
        page = 1 + (page - 1) * 2
        start_urls_s = [f'https://search.jd.com/Search?keyword={search_name}&enc=utf-8&page={page}']
        start_urls.extend(start_urls_s)
    def parse(self, response):
        search_name = []
        pic_urls_s = []
        shop_urls_s = []
        jd_item = JdItem()
        # jd_item['store_names'] = response.xpath("//li/div[@class='gl-i-wrap']/div[@class='p-shop']/span[@class='J_im_icon']/a[@class='curr-shop hd-shopname']/@title").getall()
        jd_item['shop_names'] = response.xpath('//li[@class="gl-item"]/div/div[@class="p-name p-name-type-2"]/a/@title').getall()
        jd_item['prices'] = response.xpath('//li[@class="gl-item"]/div/div[@class="p-price"]/strong/i/text()').getall()
        shop_urls = response.xpath('//li[@class="gl-item"]/div/div[@class="p-img"]/a/@href').getall()
        for i in shop_urls:
            if i[:6] == 'https:':
                shop_urls_s.append(i)
            else:
                shop_urls_s.append('https:' + i)
        jd_item['shop_urls'] = shop_urls_s

        pic_urls = response.xpath('//li[@class="gl-item"]/div/div[@class="p-img"]/a/img/@source-data-lazy-img').getall()
        for i in pic_urls:
            pic_urls_s.append('https:' + i)
        for i in range(len(jd_item['shop_urls'])):
            search_name.append(self.search_name)
        jd_item['pic_urls'] = pic_urls_s
        jd_item['search_name'] = search_name
        yield jd_item

