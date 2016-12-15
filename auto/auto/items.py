# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import datetime as dt
import scrapy

from . import models


class ErrorItem(scrapy.Item):
    error = scrapy.Field()


class AutoItem(scrapy.Item):
    brand = scrapy.Field()
    model = scrapy.Field()
    price = scrapy.Field()

    def save(self):
        created = False

        try:
            # Trying to get object if it exists.
            auto_price = models.AutoPrice.get(brand=self['brand'], model=self['model'])
        except models.AutoPrice.DoesNotExist:
            # Object does not exist.
            auto_price = models.AutoPrice.create(**self)
            created = True
        else:
            # Just update with current price and scraping time.
            auto_price.pice = self['price']
            auto_price.scraped_at = dt.datetime.now()
            auto_price.save()

        return auto_price, created
