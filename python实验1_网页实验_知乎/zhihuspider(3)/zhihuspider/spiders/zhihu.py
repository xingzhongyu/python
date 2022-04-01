import scrapy
import re
import json
import time
from zhihuspider.items import User,Posts
import zhihuspider.proxy as p
class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/cao-feng-ze-37/following']
    # P=p.GetProxy2()
    # proxies = P.GetList()
    def parse(self, response):
        x = response.body.decode('utf-8')
        pattern=re.compile(r'"urlToken":".*?"')
        y = pattern.findall(x)
        # time.sleep(3)
        for u in y[1:]:
            # print(u[12:-1])
            url="https://www.zhihu.com/people/{}/following".format(u[12:-1])
            url_post="https://www.zhihu.com/people/{}/posts".format(u[12:-1])
            yield scrapy.Request(url=url,callback=self.parse)
            yield scrapy.Request(url=url_post,callback=self.parse_detail)
            # print(y[1][12:-1])
            # print(x)
            # 用utf8解码响应的数据流
        item=User()
        name=response.xpath("//*[@id='ProfileHeader']/div/div[2]/div/div[2]/div[1]/h1/span[1]/text()").extract_first()
        info=response.xpath("//*[@id='ProfileHeader']/div/div[2]/div/div[2]/div[1]/h1/span[2]/text()").extract_first()
        followers=response.xpath("//*[@id='root']/div/main/div/div[2]/div[2]/div[2]/div/a[2]/div")
        like=response.xpath("//*[@id='root']/div/main/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/text()").extract_first()
        
        pattern3=re.compile("<meta itemProp=\"zhihu:followerCount\" content=\"(.*?)\"/>")
        fo=pattern3.search(x)
        if(fo!=None):
            followers=fo.group(1)
        else:
            followers=None
        # print(x)
        pattern2 = re.compile('\d+\.?\d*')
        if like!=None:
            like=''.join(pattern2.findall(like))
        item["name"]=name
        item["info"]=info
        item["followers"]=followers
        item["like"]=like
        if(item["name"]!=None):
            print(item)
    def parse_detail(self,response):
        x=response.body.decode("utf-8")
        # print(x)
        pattern2=re.compile(r'\\u003C.*?\\u003E')
        pattern3=re.compile(r'"voteupCount":\d+,"')
        pattern=re.compile('"content":".*?",')
        for s,v in zip(re.findall(pattern,x),re.findall(pattern3,x)):
            post=Posts()
            post["content"]=re.sub(pattern2," ",s)[12:]
            post["voteCount"]=v[14:-2]
            if(post["content"]!=None):
                print(post)
