#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from scrapy import cmdline
# search_name = '手机'
# cmdline.execute('scrapy crawl jd'.split())
# cmdline.execute('scrapy crawl yhd'.split())
# cmdline.execute('scrapy crawl kaolao'.split())
# cmdline.execute(['scrapy', 'rawl', 'jd'])
cmdline.execute('scrapy crawlall'.split())