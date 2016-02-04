import scrapy
from lianjia.items import lianjiaItem

class lianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ["lianjia.com"]
    city_and_page = {
            'dongcheng': 99, 'cicheng': 100, 'chaoyang': 100, 'haidian': 100,
            'fengtai': 100, 'shijingshan': 96, 'tongzhou': 93, 'changping': 100,
            'daxing': 100, 'yizhuangkaifaqu': 52, 'shunyi': 100, 'fangshan': 100, 
            'mentougou': 49, 'pinggu': 0, 'huairou': 1, 'miyun': 1, 'yanqing': 1,
            'yanjiao': 100}
    start_urls = []
    for i in range(100):
        start_urls.append("http://bj.lianjia.com/ershoufang/xicheng/pg%s" % str(i+1))

    def parse(self, response):
        for sel in response.xpath("//div[@class='info-panel']"):
            lianjia = lianjiaItem()
            lianjia['name_of_community'] = sel.xpath("div[1]/div[1]/a/span/text()").extract()
            lianjia['layout_of_house'] = sel.xpath("div[1]/div[1]/span[1]/span/text()").extract()
            lianjia['price_of_house'] = sel.xpath("div[2]/div[1]/span/text()").extract()
            lianjia['area_of_house'] = sel.xpath("div[1]/div[1]/span[2]/text()").extract()
            lianjia['time_of_construction'] = sel.xpath("div[1]/div[2]/div/text()").extract() 
            
            yield lianjia
