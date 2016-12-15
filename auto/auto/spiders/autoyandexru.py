# -*- coding: utf-8 -*-
import scrapy


class AutoyandexruSpider(scrapy.Spider):
    name = "autoyandexru"
    allowed_domains = ["auto.yandex.ru"]
    start_urls = ['http://auto.yandex.ru/']

    def parse(self, response):
        pass
