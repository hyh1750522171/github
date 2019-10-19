import requests
from lxml import etree
import threading


class Spider(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
        self.offset = 1

    def start_work(self, url):
        print("正在爬取第 %d 页......" % self.offset)
        self.offset += 1
        response = requests.get(url=url, headers=self.headers)
        html = response.content.decode()
        html = etree.HTML(html)

        video_src = html.xpath('//div[@class="video-play"]/video/@src')
        video_title = html.xpath('//span[@class="video-title"]/text()')
        next_page = "http:" + html.xpath('//a[@class="next"]/@href')[0]
        # 爬取完毕...
        if next_page == "http:":
            return

        self.write_file(video_src, video_title)
        self.start_work(next_page)

    def write_file(self, video_src, video_title):
        for src, title in zip(video_src, video_title):
            response = requests.get("http:" + src, headers=self.headers)
            file_name = title + ".mp4"
            file_name = "".join(file_name.split("/"))
            print("正在抓取%s" % file_name)
            with open(file_name, "wb") as f:
                f.write(response.content)


if __name__ == "__main__":
    spider = Spider()
    for i in range(0, 3):
        # spider.start_work(url="https://ibaotu.com/shipin/7-0-0-0-"+ str(i) +"-1.html")
        t = threading.Thread(target=spider.start_work,
                             args=("https://ibaotu.com/shipin/7-0-0-0-0-2.html" + str(i) + "-1.html",))
        t.start()
