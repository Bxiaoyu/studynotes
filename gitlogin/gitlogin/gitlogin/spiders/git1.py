import scrapy


class Git1Spider(scrapy.Spider):
    name = 'git1'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/exile-morganna']

    def start_requests(self):
        url = self.start_urls[0]
        temp = "finger=1571944565; " \
               "_uuid=AE4C631A-2D3B-7DB7-6B25-DC7F1DB86AFC53294infoc; " \
               "buvid3=71221713-D985-4561-8037-6E9040B6F23070403infoc; " \
               "sid=6a4ami2l; DedeUserID=315883985; DedeUserID__ckMd5=206216d00a419151; " \
               "SESSDATA=260b77d4%2C1611064869%2C0cbee*71; bili_jct=6f47d9a661f7d9beb86a769be06b94ec; " \
               "CURRENT_FNVAL=16; rpdid=|(J~J)kRJ)uJ0J'ulmlluJuku; bp_video_offset_315883985=415220842424899150; " \
               "bp_t_offset_315883985=415220842424899150"

        cookies = {data.split("=")[0]:data.split("=")[-1] for data in temp.split("; ")}
        yield scrapy.Request(
            url=url,
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(response.xpath('/html/head/title/text()').extract_first())
