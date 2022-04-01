#!/usr/bin/env python 
# -- coding: utf-8 -- 

from scrapy import signals
from .myextend import pro
from w3lib.http import basic_auth_header
import random


class ProxyDownloaderMiddleware:

    def process_request(self, request, spider):
        proxy = random.choice(pro.proxy_list)
        request.meta['proxy'] = "http://%(proxy)s" % {'proxy': proxy}
        # 用户名密码认证(私密代理/独享代理)
        username="xzy12386"
        password="pbgu6g34"
        request.headers['Proxy-Authorization'] = basic_auth_header("xzy12386", "pbgu6g34")  # 白名单认证可注释此行
        return None