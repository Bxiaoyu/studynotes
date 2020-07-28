import scrapy
from Douban.items import DoubanItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        el_list = response.xpath('//*[@class="info"]')
        print(response.request.headers["User-Agent"])

        for el in el_list:
            item = DoubanItem()

            item['name'] = el.xpath('./div[1]/a/span[1]/text()').extract_first()
            item['info'] = el.xpath('./div[2]/p[1]/text()').extract_first().strip()
            item['score'] = el.xpath('./div[2]/div/span[2]/text()').extract_first()
            item['desc'] = el.xpath('./div[2]/p[2]/span/text()').extract_first()
            yield item

        url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if url != None:
            url = response.urljoin(url)
            yield scrapy.Request(
                url=url
            )
