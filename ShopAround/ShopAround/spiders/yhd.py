# -*- coding: utf-8 -*-
import re
import scrapy
from ShopAround.items import YhdItem

class YhdSpider(scrapy.Spider):
    start_urls = []
    name = 'yhd'
    allowed_domains = ['yhd.com']
    search_name = input('你输入想要查询一号店的商品名称: ')
    pages = int(input('你输入想要爬取一号店的商品页数: '))

    for page in range(1, pages):
        start_urls_s = ['https://search.yhd.com/c0-0/k' + search_name + '/#page=' + str(page) +'&sort=1']
        start_urls.extend(start_urls_s)

    def parse(self, response):
        yhd_item = YhdItem()
        html = response.text
        shop_urls_s = re.findall('href="(.*?)" target="_blank" isSeiralCombine="0"', html)  # 商品url
        shop_urls_s1 = []
        pic_urls_s = response.xpath('//div[@id="searchProImg"]/a[@class="img"]/img/@src').getall()  # 图片url
        pic_urls_ss = response.xpath('//div[@id="searchProImg"]/a[@class="img"]/img/@original').getall()  # 图片url
        pic_urls_s1 = []
        search_name = []
        for i in shop_urls_s:
            shop_urls_s1.append('https:' + i)
        for i in pic_urls_s:
            pic_urls_s1.append('https:' + i)
        for i in pic_urls_ss:
            pic_urls_s1.append('https:' + i)
        for i in range(len(shop_urls_s)):
            search_name.append(self.search_name)
        # yhd_item['store_names'] = re.findall('<span class="shop_text">(.*?)</span>', html)
        yhd_item['shop_names'] = re.findall('title="(.*?)" singleFreeFlag="0"', html)
        yhd_item['prices'] = re.findall('yhdPrice="(.*?)"', html)
        yhd_item['shop_urls'] = shop_urls_s1
        yhd_item['pic_urls'] = pic_urls_s1
        yhd_item['search_name'] = search_name

        yield yhd_item
