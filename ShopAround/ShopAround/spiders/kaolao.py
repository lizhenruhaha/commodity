# -*- coding: utf-8 -*-
import scrapy
from ShopAround.items import KaolaoItem
class KaolaoSpider(scrapy.Spider):
    start_urls=[]
    name = 'kaolao'
    allowed_domains = ['search.kaolao.com']
    search_name = input('你输入想要查询的考拉商品名称: ')
    pages = int(input('你输入想要爬取考拉的商品页数: '))
    # pages = 10
    for page in range(1, pages):
        start_urls_s = [f'https://search.kaola.com/search.html?key={search_name}&pageNo={page}']
        start_urls.extend(start_urls_s)

    def parse(self, response):
        search_name = []
        pic_urls_s = []
        shop_urls_s = []
        kaolao_item = KaolaoItem()
        kaolao_item['shop_names'] = response.xpath('//*[@id="result"]/li/div/a/@title').getall()
        kaolao_item['prices'] = response.xpath('//*[@id="result"]/li/div/div[2]/p[1]/span[1]/text()').getall()

        shop_urls = response.xpath('//*[@id="result"]/li/div/a/@href').getall()
        for i in shop_urls:
            shop_urls_s.append('https:' + i)
        kaolao_item['shop_urls'] = shop_urls_s

        pic_urls = response.xpath('//*[@id="result"]/li/div/a/div/img/@data-src').getall()
        for i in pic_urls:
            pic_urls_s.append('https:' + i)
        for i in range(len(kaolao_item['shop_urls'])):
            search_name.append(self.search_name)
        kaolao_item['pic_urls'] = pic_urls_s
        kaolao_item['search_name'] = search_name

        yield kaolao_item
