import scrapy
from myscrapy.items  import MyscrapyItem


class Spider(scrapy.Spider):
    #爬虫名
    name = "myspider"
    #起始链接
    start_urls = ['http://www.jjwxc.net/fenzhan/yq/']


    def parse(self, response):
        #开始爬取
        print("spider start")
        #取出所有<li>标签中style=_width:183px;的标签
        node_list = response.xpath("//li[@style='_width:183px;']")

        #遍历list
        for node in node_list:
            # 创建item字段对象用来存储信息
            item = MyscrapyItem()
            # extract() : 将xpath对象转换为Unicode字符串
            novelName= node.xpath("./a/@alt").extract()
            authorName = node.xpath("./a/label/text()").extract()
            novelContent= node.xpath("./a/@href").extract()

            #对的到的信息进行一点加工,并放入item中
            item['novelName'] = novelName[0].split(" ")[0]
            item['authorName'] = authorName[0]
            item['novelContent'] = "http://www.jjwxc.net/"+novelContent[0]



            yield item
