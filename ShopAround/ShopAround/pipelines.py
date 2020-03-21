# # -*- coding: utf-8 -*-
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from ShopAround.database_connect import HOST,DB,PASSWORD,PORT,USER
import pymysql.cursors
class ShoparoundPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=HOST,
            port=PORT,
            db=DB,
            user=USER,
            passwd=PASSWORD,
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        for i in range(len(item['prices'])):
            self.cursor.execute(
            """insert into info(shop_names, prices, shop_urls, pic_urls, search_name)
            value (%s, %s, %s, %s, %s)""",
            (
             item['shop_names'][i],
             item['prices'][i],
             item['shop_urls'][i],
             item['pic_urls'][i],
             item['search_name'][i]))
            self.connect.commit() # 提交
        return item

