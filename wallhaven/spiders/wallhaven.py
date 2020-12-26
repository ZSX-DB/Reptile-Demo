from scrapy import Spider, Request

class QuotesSpider(Spider):
    name = "wallhaven"
    # start_urls = [
    #     'https://wallhaven.cc/toplist?page=1',
    #     'https://wallhaven.cc/toplist?page=2'
    # ]

    # 此种方法无法生成动态url
    # start_url = []
    # for i in range(1, 7):
    #     start_url.append('https://wallhaven.cc/toplist?page=' + str(i))

    # 动态生成初始URL
    def start_requests(self):
        for i in range(1, 5):
            url = 'https://wallhaven.cc/toplist?page={p}'.format(p=i)
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        for li in response.css('li'):
            yield {
                'href': li.css('a.preview::attr(href)').get(),
                'img_src': li.css('img::attr(data-src)').get()
            }
