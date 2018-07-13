# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from chinabidding.items import ChinabiddingItem

from scrapy.conf import settings







class ChinabiddingspiderSpider(CrawlSpider):
    keyword = settings.get("KEYWORDS")

    url="https://www.chinabidding.cn/search/searchzbw/search2?areaid=&keywords={keyword}&page=1&categoryid=&rp=22&table_type=0&b_date=month"

    name = 'chinabiddingSpider'
    allowed_domains = ['chinabidding.cn']
    start_urls = [(url.format(keyword =keyword ))]

    rules = (
        Rule(LinkExtractor(allow=r'&page=\d+&categoryid=&'), callback='parse_item1', follow=True),
    )

    def parse_item1(self, response):
        item = ChinabiddingItem()
        for node in response.xpath("(//tbody/tr[@class='listrow2']|//tbody/tr[@class='listrow1'])"):
            item["positionName"] = node.xpath("./td[2]/a/text()").extract()[0].strip()  # 职位名称
            item["positiontype"] = node.xpath("./td[4]/text()").extract()[0].strip()  # 职位类别
            item["publishtime"] = node.xpath("./td[7]/text()").extract()[0].strip()  # 发布时间
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return item
