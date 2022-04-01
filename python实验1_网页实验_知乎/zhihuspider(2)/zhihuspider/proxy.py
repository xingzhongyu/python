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
PROXY_POOL_URL = 'http://localhost:5555/random'
class GetProxy3(object):
    def __init__(self):
        super().__init__()  
    def get_proxy(self):
        try:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                return [response.text]
        except ConnectionError:
            return None
class GetProxy2(object):
    def __init__(self):
        super().__init__()
    def GetList(self):
        url = "http://dps.kdlapi.com/api/getdps/?orderid=942270314434172&num=10&pt=1&format=json&sep=1"
        # res = requests.get(url)
        # print(res.content)
        # proxy=res.content
        proxy=['113.128.24.229:20310','114.99.130.238:22597','114.100.1.4:15037','182.87.136.44:23849','116.209.102.37:20004','49.84.29.154:18813','114.99.196.55:21423','124.229.172.102:17303','113.218.237.242:19521','180.127.240.213:20126'
        ,'113.128.26.209:18837','117.57.98.34:16694','111.225.152.192:22108','114.216.130.117:17355','120.38.237.87:16568','182.34.199.224:22325', '175.7.196.81:23233', '27.156.193.142:23940',
         '182.134.156.12:22248', '220.201.84.238:19389', '116.115.211.198:15252', '113.206.16.139:15952', '113.101.254.243:20476', '27.29.155.0:21197', '36.57.199.201:18534']
        # proxy=json.loads(res.content)["data"]["proxy_list"]
        # print(proxy[0])
        print(proxy)
        lists=[]
        for p in proxy:
            proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": p},
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
# class GetProxy2(object):
#     def __init__(self):
#         super().__init__()
#     def GetList(self):
#         api_url = "http://dps.kdlapi.com/api/getdps/?orderid=9266892014xxxxx&num=1&pt=1&sep=1"
#         # s='''{"code":200,"msg":"ok","data":[{"ip":"113.117.67.132","port":5412,"expire_time":"2021-06-02 09:20:14","city":"\u63ed\u9633","isp":"\u7535\u4fe1"},{"ip":"114.238.54.89","port":766,"expire_time":"2021-06-02 09:20:23","city":"\u6dee\u5b89","isp":"\u7535\u4fe1"},{"ip":"114.227.162.133","port":3617,"expire_time":"2021-06-02 09:20:13","city":"\u5e38\u5dde","isp":"\u7535\u4fe1"},{"ip":"58.255.198.145","port":36410,"expire_time":"2021-06-02 09:20:15","city":"\u60e0\u5dde","isp":"\u8054\u901a"},{"ip":"61.191.85.57","port":766,"expire_time":"2021-06-02 09:28:39","city":"\u94dc\u9675","isp":"\u7535\u4fe1"},{"ip":"125.126.110.90","port":894,"expire_time":"2021-06-02 10:06:12","city":"\u53f0\u5dde","isp":"\u7535\u4fe1"},{"ip":"220.175.214.153","port":766,"expire_time":"2021-06-02 09:20:16","city":"\u666f\u5fb7\u9547","isp":"\u7535\u4fe1"},{"ip":"60.189.202.66","port":5412,"expire_time":"2021-06-02 10:06:51","city":"\u53f0\u5dde","isp":"\u7535\u4fe1"},{"ip":"124.112.171.111","port":3617,"expire_time":"2021-06-02 09:10:27","city":"\u9a6c\u978d\u5c71","isp":"\u7535\u4fe1"},{"ip":"36.56.102.2","port":894,"expire_time":"2021-06-02 10:10:13","city":"\u9a6c\u978d\u5c71","isp":"\u7535\u4fe1"},{"ip":"60.174.190.13","port":766,"expire_time":"2021-06-02 10:05:39","city":"\u9a6c\u978d\u5c71","isp":"\u7535\u4fe1"},{"ip":"115.202.201.134","port":894,"expire_time":"2021-06-02 10:06:31","city":"\u53f0\u5dde","isp":"\u7535\u4fe1"},{"ip":"183.94.210.201","port":3617,"expire_time":"2021-06-02 10:10:17","city":"\u968f\u5dde","isp":"\u8054\u901a"},{"ip":"36.56.103.246","port":766,"expire_time":"2021-06-02 10:05:48","city":"\u9a6c\u978d\u5c71","isp":"\u7535\u4fe1"},{"ip":"114.100.1.210","port":766,"expire_time":"2021-06-02 09:20:21","city":"\u9a6c\u978d\u5c71","isp":"\u7535\u4fe1"},{"ip":"220.179.211.219","port":23564,"expire_time":"2021-06-02 09:33:45","city":"\u94dc\u9675","isp":"\u7535\u4fe1"},{"ip":"49.87.140.153","port":3617,"expire_time":"2021-06-02 09:20:17","city":"\u6dee\u5b89","isp":"\u7535\u4fe1"},{"ip":"114.100.3.123","port":36410,"expire_time":"2021-05-02 15:41:14","city":"\u9a6c\u978d\u5c71","isp":"\u7535\u4fe1"},{"ip":"60.174.190.209","port":894,"expire_time":"2021-06-02 10:10:12","city":"\u9a6c\u978d\u5c71","isp":"\u7535\u4fe1"},{"ip":"183.92.74.109","port":5412,"expire_time":"2021-06-02 10:05:24","city":"\u968f\u5dde","isp":"\u8054\u901a"}]}'''
#         # l=[]
#         # for da in json.loads(s)["data"]:
#         #     proxies = {
#         #     "http": "http://{ip}:{port}".format_map({"ip":da["ip"],"port":da["port"]}),
#         #     "https": "https://{ip}:{port}".format_map({"ip":da["ip"],"port":da["port"]})
#         #     }
#         #     l.append(proxies)
#         proxy=["121.41.8.23:16817"]
#         tunnel = "tps112.kdlapi.com:15818"
#         # print(proxy[0])
#         lists=[]
#         proxies = {
#             "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
#             "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
#         }
#         lists.append(proxies)
#         print(proxies,"---------")
#         # # 要访问的目标网页
#         # target_url = "https://dev.kdlapi.com/testproxy"

#         # # # 使用代理IP发送请求
#         # try:
#         #     response = requests.get(target_url, proxies=proxies)
#         #     print(response)
#         # except Exception as e:
#         #     print(str(e))
#         return lists
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