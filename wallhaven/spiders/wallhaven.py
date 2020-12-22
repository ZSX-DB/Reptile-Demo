# import scrapy
from scrapy import Spider


class QuotesSpider(Spider):
    name = "wallhaven"
    start_urls = [
        'https://wallhaven.cc/toplist?page=1',
        'https://wallhaven.cc/toplist?page=2'
    ]

    def parse(self, response):
        for li in response.css('li'):
            yield {
                'preview': li.css('a.preview').get(),
                # 'href': li.css('figure a::attr(href)').extract()[0]
                # response.css("div.abc a::attr(href)").extract()[0]
            }
        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').get(),
        #         'author': quote.css('small.author::text').get(),
        #         'tags': quote.css('div.tags a.tag::text').getall(),
        #     }
