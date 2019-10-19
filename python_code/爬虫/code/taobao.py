import requests
import pymysql
import re
import time
import threading
import pandas as pd
from lxml import etree


# 数据请求
class Request(object):

    def __init__(self):
        pass
    # url字符串拼接
    def url(self, num):
        str1 = input("请输入你想搜索的内容")
        if num == 1:
            url = "https://search.bilibili.com/all?keyword="+str1+"&from_source=banner_search&page="
        else:
            for sj in range(2, num):
                url = "https://search.bilibili.com/all?keyword="+str1+"&from_source=banner_search&page="+sj

        return url

    # requests请求
    def reque(self,url):
        headers = {
            'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                           ' (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
        resopt = requests.get(url, headers=headers,)
        if resopt.status_code == 200:
            print('状态码是: 200 请求成功。')
        elif resopt.status_code:
            print("状态码是: %d ，请求失败" % resopt.status_code)
        return resopt.text


# 筛选数据
class dispose(object):

    def __init__(self):
        pass


# 保存到数据库
class databases(object):

    def __init__(self):
        pass
    def xpath(self, data):
        # 创建返回数据列表
        dataList = []
        html = etree.HTML(data)
        # 获取总页数
        zongyeshu = html.xpath("/html/body/div[1]/div[2]/div[3]/div[1]/div[26]/div/div/div/div[1]")

# 保存文件形式
class File():
    def __init__(self):
        pass
    def open(self):
        data = pd()




def run():
    pass

if __name__ == "__main__":
    run()