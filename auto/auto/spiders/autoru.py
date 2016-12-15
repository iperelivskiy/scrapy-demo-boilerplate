import scrapy
from auto import items


class AutoruSpider(scrapy.Spider):
    name = 'autoru'

    def start_requests(self):
        url = 'https://auto.ru/cars/nissan/juke/i/group-offroad_5d/mod-77026/statistics/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        price = response.css('.stat-header-avg .stat-header-price::text').extract_first()

        if price is not None:
            price = ''.join(price.split()[:-1])
            yield items.AutoItem(brand='Nissan', model='Juke', price=price)
        else:
            yield items.ErrorItem(error='Unable to find the price.')
