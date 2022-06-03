import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名称,用于运行爬虫的时候使用
    name = 'baidu'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']
    # 起始ur地址,第一次要访问的url, 后缀地址最好不要加斜杆/
    start_urls = ['http://www.baidu.com']

    # 执行了start_urls请求后，回调返回的方法，实际就是response = urllib.request.urlopen()
    def parse(self, response):
        print("=======百度爬虫===========")
        # text 字符串
        # print(response.text)
        # 二进制数据
        # print(response.body)
        # 不需要导入lxml,直接使用xpath
        ipt = response.xpath('//input[@id="su"]')
        print(ipt)
        print(ipt.extract())
        pass
