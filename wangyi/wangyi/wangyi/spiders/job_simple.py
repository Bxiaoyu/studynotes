import scrapy
from wangyi.items import WangyiSimpleItem


class JobSimpleSpider(scrapy.Spider):
    name = 'job_simple'
    # 检查修改allowed_domains()
    allowed_domains = ['163.com']
    # 修改start_url
    start_urls = ['https://hr.game.163.com/recruit.html']

    def parse(self, response):
        # 提取数据
        # 获取所有职位节点
        node_list = response.xpath('//*[@class="list-header clearfix"]')
        # print(len(node_list))
        # 遍历节点列表
        for num, node in enumerate(node_list):
            item = WangyiSimpleItem()

            # 设置过滤条件，将目标节点数据提取出来，同时去除前后空格以及换行符
            item['name'] = node.xpath('./li[2]/p/a/text()').extract_first().strip()
            item['link'] = node.xpath('./li[2]/p/a/@href').extract_first()
            item['depart'] = node.xpath('./li[3]/p/text()').extract_first().strip()
            item['type'] = node.xpath('./li[4]/p/text()').extract_first()
            item['address'] = node.xpath('./li[5]/p/span/text()').extract_first().strip()
            item['num'] = node.xpath('./li[6]/p/text()').extract_first().strip()
            item['date'] = node.xpath('./li[7]/p/text()').extract_first()
            # print(item)
            yield item
        # 模拟翻页
        part_url = response.xpath('//*[@class="pagination-wrap"]/li[3]/a[2]/@href').extract_first()
        print(part_url)

        # 判断终止条件
        if part_url != 'javascript:void(0);':
            # response.urljoin()用于拼接相对路径的url，可以理解为自动补全
            # next_url = response.urljoin(part_url)
            next_url = "https://hr.game.163.com" + part_url
            # 构建请求对象,并且返回给引擎
            yield scrapy.Request(url=next_url, callback=self.parse)
