# import requests
# username="t12269757575513"
# password="s9ghxj91"

# tunnel = "tps112.kdlapi.com:15818"
#         # print(proxy[0])

# proxies = {
#     "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
#     "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
# }

# # 白名单方式（需提前设置白名单）
# # proxies = {
# #     "http": "http://%(proxy)s/" % {"proxy": tunnel},
# #     "https": "http://%(proxy)s/" % {"proxy": tunnel}
# # }

# # 要访问的目标网页
# target_url = "https://www.kuaidaili.com/usercenter/tps/usestat/?realtime=1"

# # 使用隧道域名发送请求
# response = requests.get(target_url, proxies=proxies)

#         # # 使用代理IP发送请求
# try:
#     response = requests.get(target_url, proxies=proxies)
#     print(response)
# except Exception as e:
#     print(str(e))
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用requests请求代理服务器
请求http和https网页均适用
"""
username="xzy12386"
password="pbgu6g34"
import requests
import random

# 提取代理API接口，获取1个代理IP
# api_url = "http://dps.kdlapi.com/api/getdps/?orderid=9266892014xxxxx&num=1&pt=1&sep=1"

# 获取API接口返回的代理IP
# proxy_ip = requests.get(api_url).text
proxy=['113.128.24.229:20310','114.99.130.238:22597','114.100.1.4:15037','182.87.136.44:23849','116.209.102.37:20004','49.84.29.154:18813','114.99.196.55:21423','124.229.172.102:17303','113.218.237.242:19521','180.127.240.213:20126'
        ,'113.128.26.209:18837',
        '117.57.98.34:16694','111.225.152.192:22108','114.216.130.117:17355','120.38.237.87:16568','182.34.199.224:22325', '175.7.196.81:23233', '27.156.193.142:23940',
         '182.134.156.12:22248', '220.201.84.238:19389', 
         '116.115.211.198:15252', '113.206.16.139:15952', '113.101.254.243:20476', '27.29.155.0:21197', '36.57.199.201:18534'
        ]
# 用户名密码认证(私密代理/独享代理)
# username = "username"
# password = "password"
lists=[]
for p in proxy:
    proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy":p},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": p}
    }
    lists.append(proxies)

# 白名单方式（需提前设置白名单）
# proxies = {
#     "http": "http://%(proxy)s/" % {"proxy": proxy_ip},
#     "https": "http://%(proxy)s/" % {"proxy": proxy_ip}
# }

# 要访问的目标网页
target_url = "https://blog.csdn.net/weixin_43164535/article/details/82557194"

try:
    response = requests.get(target_url, proxies=proxies)
    print(response)
except Exception as e:
    print(str(e))