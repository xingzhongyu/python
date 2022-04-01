import scrapy
import re
import json
import time
from zhihuspider.items import User,Posts,Topics,Topics2
import zhihuspider.proxy as p
class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/dantes-15/following']
    P=p.GetProxy2()
    proxies = P.GetList()
    def parse(self, response):
        x = response.body.decode('utf-8')
        pattern=re.compile(r'"urlToken":".*?"')
        y = pattern.findall(x)
        # print(y)
        # print(x)
        # time.sleep(3)
        # item=Topics()
        name=response.xpath("//*[@id='ProfileHeader']/div/div[2]/div/div[2]/div[1]/h1/span[1]/text()").extract_first()
         # print(y[0])
        # info=response.xpath("//*[@id='ProfileHeader']/div/div[2]/div/div[2]/div[1]/h1/span[2]/text()").extract_first()
        # followers=response.xpath("//*[@id='root']/div/main/div/div[2]/div[2]/div[2]/div/a[2]/div")
        # like=response.xpath("//*[@id='root']/div/main/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/text()").extract_first()
        # pattern3=re.compile("<meta itemProp=\"zhihu:followerCount\" content=\"(.*?)\"/>")
        # fo=pattern3.search(x)
        # if(fo!=None):
        #     followers=fo.group(1)
        # else:
        #     followers=None
        # # print(x)
        # pattern2 = re.compile('\d+\.?\d*')
        # if like!=None:
        #     like=''.join(pattern2.findall(like))
        # item["name"]=name
        # item["info"]=info
        # item["followers"]=followers
        # item["like"]=like
        # if(item["name"]!=None):
        #     print(item)
            # yield item


        for u in y[1:]:
            # print(u[12:-1])
            url="https://www.zhihu.com/people/{}/following".format(u[12:-1])
            url_topic="https://www.zhihu.com/people/{}/following/topics".format(u[12:-1])
            yield scrapy.Request(url=url,callback=self.parse)
            # print(url_topic)
            yield scrapy.Request(url=url_topic,callback=self.parse_topic,meta={"name":name})

        # url_topic="https://www.zhihu.com/people/{}/following/topics".format(y[1][12:-1])
        # yield scrapy.Request(url=url_topic,callback=self.parse_topic,meta={"name":name})


            # url_post="https://www.zhihu.com/people/{}/posts".format(u[12:-1])
            # yield scrapy.Request(url=url_post,callback=self.parse_detail)
            # print(y[1][12:-1])
            # print(x)
            # 用utf8解码响应的数据流
        
    # def parse_detail(self,response):
    #     x=response.body.decode("utf-8")
    #     # print(x)
    #     pattern2=re.compile(r'\\u003C.*?\\u003E')
    #     pattern3=re.compile(r'"voteupCount":\d+,"')
    #     pattern=re.compile('"content":".*?",')
    #     for s,v in zip(re.findall(pattern,x),re.findall(pattern3,x)):
    #         post=Posts()
    #         post["content"]=re.sub(pattern2," ",s)[12:]
    #         post["voteCount"]=v[14:-2]
    #         if(post["content"]!=None):
    #             yield post
    def parse_topic(self,response):
        # print(response)
        # print(item)
        # print(response.xpath("//*[@id='Profile-following']/div[2]//a[@class='TopicLink']"))
        x=response.body.decode("utf-8")
        # print(x)
        # pattern=re.compile(',"name":".*?","introduction":')
        pattern2=re.compile('"id":"([0-9]+)"}')
        # to=re.findall(pattern,x)
        ton=re.findall(pattern2,x)
        # print(ton)
        for tid in ton:
            url="https://www.zhihu.com/topic/{}".format(tid)
            yield scrapy.Request(url=url,callback=self.parse_topic_detail,meta={"name":response.meta["name"]})

        # url="https://www.zhihu.com/topic/{}".format(ton[0])
        # print(ton)
        # print(url)
        # yield scrapy.Request(url=url,callback=self.parse_topic_detail,meta={"name":response.meta["name"]})

        # if to !=None and ton !=None:
            # print(to)
            # print(ton)
    def parse_topic_detail(self,response):
        x=response.body.decode("utf-8")
        # with open("text.txt","w",encoding="UTF-8") as f:
        #     f.write(x)
        con=re.compile('"introduction":"(.*?)","')
        # print(response.xpath('//*[@id="TopicMain"]/div[3]/div'))
        item=Topics2()
        item["name"]=response.meta["name"]
        t=response.xpath('//*[@id="root"]/div/main/div/div[1]/div[1]/div/div/div[2]/div/div[2]/h2/div/text()')
        if(t!=[]):
            item["title"]=t.extract_first()
            item["followers"]=response.xpath('//*[@id="root"]/div/main/div/div[2]/div/div/div/div[1]/div/button/div/strong/text()').extract_first()
            item["qnum"]=response.xpath('//*[@id="root"]/div/main/div/div[2]/div/div/div/div[1]/div/a/div/strong/text()').extract_first()
            item["des"]=re.search(con,x).group(1)
            yield item
    
        