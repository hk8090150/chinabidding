# -*- coding: utf-8 -*-
import scrapy
import sys
from ..items import ChinabiddingItem


class ChinabiddingSpiderSpider(scrapy.Spider):
    name = 'chinabidding_spider'
    allowed_domains = ['www.chinabidding.cn']
    # start_urls = ['http://www.chinabidding.cn/']
    offset = 0
    # url = 'https://www.chinabidding.cn//search/searchzbw/search2?areaid=&keywords=%E6%B9%96%E5%8D%97&page={offset}&categoryid=&rp=22&table_type=0&b_date=month'
    url = 'https://www.chinabidding.cn/search/searchzbw/search2?areaid=&keywords=%E8%8C%B6%E9%99%B5&page=1&categoryid=&rp=22&table_type=0&b_date=month'
    # 设置页码


    # 默认url
    start_urls = [url ]

    def parse(self, response):
        result = response.xpath("(//tbody/tr[@class='listrow2']|//tbody/tr[@class='listrow1'])");
        item = ChinabiddingItem()
        print("********************")
        # print(result)
        for node in result:
        #     # print(node.xpath("./td[4]/text()").extract()[0])  # 信息类别)
        #     # print(node.xpath("./td[2]/a/text()").extract()[0] )
            item["positionName"] = node.xpath("./td[2]/a/text()").extract()[0].strip()  # 职位名称
            item["positiontype"] = node.xpath("./td[4]/text()").extract()[0].strip()  # 职位类别
            item["publishtime"] = node.xpath("./td[7]/text()").extract()[0].strip()# 发布时间
        #     # item["positionLink"] = node.xpath("./td[1]/a/@href").extract()[0]  # 职位详情链接
        #     # item["positiontype"] = node.xpath("./td[2]/text()").extract()[0]  # 职位类别
        #     # item["peoplenumber"] = node.xpath("./td[3]/text()").extract()[0]  # 招聘人数
        #     # item["workLocation"] = node.xpath("./td[4]/text()").extract()[0]  # 工作地点
        #     # item["publishtime"] = node.xpath("./td[7]/text()").extract()[0]  # 发布时间
        #
        #     # print(node.xpath("./td[7]/text()").extract()[0])  # 发布时间)
        #
        #
        #
            yield item
        #     # 设置新URL页码
        # if (self.offset < 5000):
        #     self.offset += 1
        # # 把请求交给控制器
        # url2 = response.xpath("//div[@id='pages']/span/a[8]/@href")


        # print(nexthref)
        try:
            nexthref = response.xpath("//div/span/a[starts-with(text(),'后一页')]/@href").extract()[0]
            if nexthref is not None:
                next_page = response.urljoin(nexthref)
                yield scrapy.Request(next_page, callback=self.parse)

        except Exception :
            print("页面爬取完")



        # if nexthref!=0:
        #     # 将相对url转为绝对url
        #     # nexthref = response.urljoin(nexthref)
        #     print(nexthref)
        #     yield scrapy.Request(("https://www.chinabidding.cn/" + nexthref), callback=self.parse)
        # else:
        #
        #     pass




        # if len (url2)>0:
        #     yield scrapy.Request(("https://www.chinabidding.cn/"+url2.extract()[0]), callback=self.parse)




            # try:

                # next_url =

        # yield scrapy.Request( (
        #         "https://www.chinabidding.cn/"+response.xpath("//div[@id='pages']/span/a[8]/@href").extract()[0]), callback=self.parse)

            #
            # except:
            #     pass


