# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from . import items


class AutoPipeline(object):

    def process_item(self, item, spider):
        if hasattr(item, 'save') and callable(item.save):
            item.save()

        return item
