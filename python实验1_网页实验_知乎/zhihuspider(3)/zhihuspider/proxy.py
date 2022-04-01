import asyncio
import aiohttp
import time
import sys
import requests
from lxml import etree
import json
import base64

username="xzy12386"
password="pbgu6g34"
TEST_URL = 'https://www.baidu.com/'

class GetProxy2(object):
    def __init__(self):
        super().__init__()
    def GetList(self):
        # url = 'http://dps.kdlapi.com/api/getdps/?orderid=922156299554072&num=5&pt=1&format=json&sep=1'
        # res = requests.get(url)
        # print(res.content)
        proxy=['113.128.24.229:20310','114.99.130.238:22597','114.100.1.4:15037','182.87.136.44:23849','116.209.102.37:20004','49.84.29.154:18813','114.99.196.55:21423','124.229.172.102:17303','113.218.237.242:19521','180.127.240.213:20126'
        ,'113.128.26.209:18837',
        '117.57.98.34:16694','111.225.152.192:22108','114.216.130.117:17355','120.38.237.87:16568','182.34.199.224:22325', '175.7.196.81:23233', '27.156.193.142:23940',
         '182.134.156.12:22248', '220.201.84.238:19389', 
         '116.115.211.198:15252', '113.206.16.139:15952', '113.101.254.243:20476', '27.29.155.0:21197', '36.57.199.201:18534'
        ]
        # print(proxy[0])
        lists=[]
        for p in proxy:
            proxies = {
            "http":"http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": p},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": p}
            }
            lists.append(proxies)
        # # 要访问的目标网页
        # target_url = "https://dev.kdlapi.com/testproxy"

        # # 使用代理IP发送请求
        # try:
        #     response = requests.get(target_url, proxies=proxies)
        #     print(response)
        # except Exception as e:
        #     print(str(e))
        return lists
# class GetProxy(object):
#     def __init__(self):
#         self.TEST_URL = TEST_URL
#         self.VALID_STATUS_CODES = [200]
#         self.usable = set()

#     def crawl_66ip(self):
#         proxies = set()
#         url = 'http://dps.kdlapi.com/api/getdps/?orderid=922156299554072&num=1&pt=1&format=json&sep=1'
#         res = requests.get(url)
#         proxies=json.loads(res.content)['data']['proxy_list']
#         print(proxies)
#         # res.encoding = "gbk"
#         # html = etree.HTML(res.text)
#         #//*[@id="list"]/table/tbody/tr[1]/td[1]
#         # lst = html.xpath('//*[@id="list"]//table//tr[position()>1]')
#         # for i in lst:
#         #     ip = i.xpath('.//td/text()')[0]
#         #     port = i.xpath('.//td/text()')[1]
#         #     proxy = ip + ':' + port
#         #     proxies.add(proxy)
#         return proxies

#     async def test_single_proxy(self, proxy):
#         conn = aiohttp.TCPConnector(ssl=False)
#         async with aiohttp.ClientSession(connector=conn) as session:
#             try:
#                 if isinstance(proxy, bytes):
#                     proxy = proxy.decode('utf-8')
#                 real_proxy = "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy}
#                 async with session.get(TEST_URL, proxy=real_proxy, timeout=20, allow_redirects=False) as response:
#                     if response.status in self.VALID_STATUS_CODES:
#                         self.usable.add(proxy)
#                         print('代理可用', proxy)
#                     else:
#                         print('请求响应码不合法 ', response.status, 'IP', proxy)
#             except Exception as e:
#                 print('代理请求失败', proxy,str(e))

#     def run(self):
#         proxies = self.crawl_66ip()
#         print('爬取代理个数为：%d' % len(proxies))
#         print('开始测试：\n')
#         loop = asyncio.get_event_loop()
#         tasks = [self.test_single_proxy(proxy) for proxy in proxies]
#         loop.run_until_complete(asyncio.wait(tasks))
#         sys.stdout.flush()
#         time.sleep(5)

#     def get_proxy_list(self):
#         self.run()
#         print('可用代理个数为：%d' % len(self.usable))
#         print(self.usable)
#         return list(self.usable)