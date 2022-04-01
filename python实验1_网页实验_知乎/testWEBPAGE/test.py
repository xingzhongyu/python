import json
s='''{"code":200,"msg":"ok","data":[{"ip":"113.117.67.132","port":5412,"expire_time":"2021-06-02 09:20:14","city":"\u63ed\u9633","isp":"\u7535\u4fe1"},{"ip":"114.238.54.89","port":766,"expire_time":"2021-06-02 09:20:23","city":"\u6dee\u5b89","isp":"\u7535\u4fe1"},{"ip":"114.227.162.133","port":3617,"expire_time":"2021-06-02 09:20:13","city":"\u5e38\u5dde","isp":"\u7535\u4fe1"},{"ip":"58.255.198.145","port":36410,"expire_time":"2021-06-02 09:20:15","city":"\u60e0\u5dde","isp":"\u8054\u901a"},{"ip":"61.191.85.57","port":766,"expire_time":"2021-06-02 09:28:39","city":"\u94dc\u9675","isp":"\u7535\u4fe1"},{"ip":"125.126.110.90","port":894,"expire_time":"2021-06-02 10:06:12","city":"\u53f0\u5dde","isp":"\u7535\u4fe1"},{"ip":"220.175.214.153","port":766,"expire_time":"2021-06-02 09:20:16","city":"\u666f\u5fb7\u9547","isp":"\u7535\u4fe1"},{"ip":"60.189.202.66","port":5412,"expire_time":"2021-06-02 10:06:51","city":"\u53f0\u5dde","isp":"\u7535\u4fe1"},{"ip":"124.112.171.111","port":3617,"expire_time":"2021-06-02 09:10:27","city":"\u9a6c\u978d\u5c71","isp":"\u7535\u4fe1"},{"ip":"36.56.102.2","port":894,"expire_time":"2021-06-02 10:10:13","city":"\u9a6c\u978d\u5c71","isp":"\u7535\u4fe1"},{"ip":"60.174.190.13","port":766,"expire_time":"2021-06-02 10:05:39","city":"\u9a6c\u978d\u5c71","isp":"\u7535\u4fe1"},{"ip":"115.202.201.134","port":894,"expire_time":"2021-06-02 10:06:31","city":"\u53f0\u5dde","isp":"\u7535\u4fe1"},{"ip":"183.94.210.201","port":3617,"expire_time":"2021-06-02 10:10:17","city":"\u968f\u5dde","isp":"\u8054\u901a"},{"ip":"36.56.103.246","port":766,"expire_time":"2021-06-02 10:05:48","city":"\u9a6c\u978d\u5c71","isp":"\u7535\u4fe1"},{"ip":"114.100.1.210","port":766,"expire_time":"2021-06-02 09:20:21","city":"\u9a6c\u978d\u5c71","isp":"\u7535\u4fe1"},{"ip":"220.179.211.219","port":23564,"expire_time":"2021-06-02 09:33:45","city":"\u94dc\u9675","isp":"\u7535\u4fe1"},{"ip":"49.87.140.153","port":3617,"expire_time":"2021-06-02 09:20:17","city":"\u6dee\u5b89","isp":"\u7535\u4fe1"},{"ip":"114.100.3.123","port":36410,"expire_time":"2021-05-02 15:41:14","city":"\u9a6c\u978d\u5c71","isp":"\u7535\u4fe1"},{"ip":"60.174.190.209","port":894,"expire_time":"2021-06-02 10:10:12","city":"\u9a6c\u978d\u5c71","isp":"\u7535\u4fe1"},{"ip":"183.92.74.109","port":5412,"expire_time":"2021-06-02 10:05:24","city":"\u968f\u5dde","isp":"\u8054\u901a"}]}'''
l=[]
for da in json.loads(s)["data"]:
    l.append("http://{ip}:{port}".format_map({"ip":da["ip"],"port":da["port"]}))
print(l)