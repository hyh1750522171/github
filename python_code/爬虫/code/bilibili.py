import requests
import pymysql
import time
import threading
import pandas as pd
from lxml import etree
import os
import xlsxwriter


# 数据请求
class Request(object):

    def __init__(self):
        pass

    # url字符串拼接
    def url(self, num):

        # if num == 1:
        url = "https://search.bilibili.com/all?keyword=" + num + "&from_source=banner_search&page="
        # else:
        #     for sj in range(2, num):
        #         url = "https://search.bilibili.com/all?keyword="+num+"&from_source=banner_search&page="+sj

        return url

    # requests请求
    def reque(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
        resopt = requests.get(url, headers=headers, )
        if resopt.status_code == 200:
            print('状态码是: 200 请求成功。')
        elif resopt.status_code:
            print("状态码是: %d ，请求失败" % resopt.status_code)
        return resopt.text


# 保存文件形式
class File(object):
    def __init__(self):
        pass

    # 打开文件
    def open(self):
        data = pd()

    # 创建目录
    def makdir(self):
        sel = input("请输入你想要保存的目录:")
        if not os.path.exists(sel):
            os.mkdir(sel)

    # 创建文件
    def touch(self):
        sel = input("请输入你想要保存的excel名字:")

        xlsxwriter.Workbook(sel)


# 筛选数据
class dispose(object):

    def __init__(self):
        pass

    def xpath(self, data):
        # 创建返回数据列表
        dataList = []
        html = etree.HTML(data)
        xxx = html.xpath("")

        if xxx > 20:
            pass
        # 标题
        biaoti = html.xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li/div/div[1]/a")
        # 上传时间
        shangchuangtime = html.xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li/div/div[3]/span[3]/text()')
        # 播放量
        bofangliang = html.xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li/div/div[3]/span[1]/text()')
        # 弹目总数
        tanmuzongshu = html.xpath(
            "/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul[2]/li[2]/div/div[3]/span[1]/text()")
        # UP主名字
        UPzhu = html.xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul[2]/li[2]/div/div[3]/span[4]/a")
        # 链接地址
        lianjiedizhi = html.xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul[2]/li[1]/div/div[1]/a/@href")
        # 获取页数
        yeshu = html.xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[3]/div/ul/li[8]/button')
        return dataList


class MysqlHelper(object):

    def __init__(self):
        pass

    @property
    # 登录数据库
    def connectdb(self):
        print('连接到mysql服务器...')
        # 打开数据库连接
        # 用户名:hp, 密码:Hp12345.,用户名和密码需要改成你自己的mysql用户名和密码，并且要创建数据库TESTDB，并在TESTDB数据库中创建好表Student
        db = pymysql.connect("localhost", "hp", "Hp12345.", "TESTDB")
        print('连接上了!')
        return db

    def createtable(self, db):
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 如果存在表Sutdent先删除
        cursor.execute("DROP TABLE IF EXISTS Student")
        sql = """CREATE TABLE Student (
                ID CHAR(10) NOT NULL,
                Name CHAR(8),
                Grade INT )"""

        # 创建Sutdent表
        cursor.execute(sql)

    def updatedb(self, db):
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 更新语句
        sql = "UPDATE Student SET Grade = Grade + 3 WHERE ID = '%s'" % ('003')

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            print('更新数据失败!')
            # 发生错误时回滚
            db.rollback()

    # 关闭数据库
    def closedb(self, db):
        db.close()


# 创建多线程类
class Threading(object):

    def __init__(self):
        pass

    # 线程1
    def oneThreading(self):
        t1 = threading.active_count()
        return t1
        pass

    # 线程2
    def towThreading(self):
        t2 = threading.active_count()
        return t2
        pass

    # 线程关闭
    def close(self):
        threading.close

class daili(object):

    def __init__(self):
        pass

    def dailiip(self):
        pass



def main():
    str1 = input("请输入你想搜索的内容:")
    data = Request()
    url = data.url(str1)
    data1 = data.reque(url)
    print(data1)
    # data_dispose = dispose()
    # data_dispose.xpath(data1)
    time.sleep(5)
    file = File()
    file.makdir()

    # 创建数据库
    '''
    ac = MysqlHelper()
    db = ac.connectdb  # 连接MySQL数据库
    db.createtable(db)  # 创建表
    db.insertdb(db)  # 插入数据
    print('\n插入数据后:')
    db.querydb(db)
    db.deletedb(db)  # 删除数据
    print('\n删除数据后:')
    db.querydb(db)
    ac.updatedb(db)  # 更新数据
    print('\n更新数据后:')
    db.querydb(db)
    ac.closedb(db)  # 关闭数据库
    '''

if __name__ == '__main__':
    main()
