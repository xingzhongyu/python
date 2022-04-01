#!/usr/bin/env python 
# -- coding: utf-8 -- 
import time
import threading

import requests
from scrapy import signals

# 提取代理IP的api
api_url = 'http://dps.kdlapi.com/api/getdps/?orderid=92021373170xxxx&num=10&pt=1&format=json&sep=1'
foo = True

class Proxy:

    def __init__(self, ):
        self._proxy_list =['113.128.24.229:20310','114.99.130.238:22597','114.100.1.4:15037','182.87.136.44:23849','116.209.102.37:20004','49.84.29.154:18813','114.99.196.55:21423','124.229.172.102:17303','113.218.237.242:19521','180.127.240.213:20126'
        ,'113.128.26.209:18837',
        '117.57.98.34:16694','111.225.152.192:22108','114.216.130.117:17355','120.38.237.87:16568','182.34.199.224:22325', '175.7.196.81:23233', '27.156.193.142:23940',
         '182.134.156.12:22248', '220.201.84.238:19389', 
         '116.115.211.198:15252', '113.206.16.139:15952', '113.101.254.243:20476', '27.29.155.0:21197', '36.57.199.201:18534'
        ]

    @property
    def proxy_list(self):
        return self._proxy_list

    @proxy_list.setter
    def proxy_list(self, list):
        self._proxy_list = list


pro = Proxy()
print(pro.proxy_list)


class MyExtend:

    def __init__(self, crawler):
        self.crawler = crawler
        # 将自定义方法绑定到scrapy信号上,使程序与spider引擎同步启动与关闭
        # scrapy信号文档: https://www.osgeo.cn/scrapy/topics/signals.html
        # scrapy自定义拓展文档: https://www.osgeo.cn/scrapy/topics/extensions.html
        crawler.signals.connect(self.start, signals.engine_started)
        crawler.signals.connect(self.close, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def start(self):
        t = threading.Thread(target=self.extract_proxy)
        t.start()

    def extract_proxy(self):
        while foo:
            pro.proxy_list =['113.128.24.229:20310','114.99.130.238:22597','114.100.1.4:15037','182.87.136.44:23849','116.209.102.37:20004','49.84.29.154:18813','114.99.196.55:21423','124.229.172.102:17303','113.218.237.242:19521','180.127.240.213:20126'
        ,'113.128.26.209:18837',
        '117.57.98.34:16694','111.225.152.192:22108','114.216.130.117:17355','120.38.237.87:16568','182.34.199.224:22325', '175.7.196.81:23233', '27.156.193.142:23940',
         '182.134.156.12:22248', '220.201.84.238:19389', 
         '116.115.211.198:15252', '113.206.16.139:15952', '113.101.254.243:20476', '27.29.155.0:21197', '36.57.199.201:18534'
        ]
            time.sleep(1800)

    def close(self):
        global foo
        foo = False