import scrapy
import re

class ZhihupinsSpider(scrapy.Spider):
    name = 'zhihupins'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/dantes-15/posts']


    def parse(self, response):
        x=response.body.decode("utf-8")
        # print(x)
        pattern2=re.compile(r'\\u003C.*?\\u003E')
        pattern3=re.compile(r'"voteupCount":\d+,"')
        pattern=re.compile('"content":".*?",')
        for s,v in zip(re.findall(pattern,x),re.findall(pattern3,x)):
            print(re.sub(pattern2," ",s)[12:])
            # print(v[14:-2])
