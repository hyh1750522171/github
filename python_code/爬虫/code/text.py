import os
str1 = ""
url = "https://s.taobao.com/search?q=java&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20191011&ie=utf8"
url = "https://s.taobao.com/search?q="+str1+"&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20191011&ie=utf8"
url = "https://s.taobao.com/search?q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20191011&ie=utf8&bcoffset=4&p4ppushleft=1%2C48&s=44&ntoffset=4"
url = "https://s.taobao.com/search?q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20191011&ie=utf8&bcoffset=4&p4ppushleft=1%2C48&ntoffset=4&s=0"
url = "https://s.taobao.com/search?q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20191011&ie=utf8&bcoffset=1&p4ppushleft=1%2C48&s=88&ntoffset=1"
sel = input("请输入你想要保存的目录")
if not os.path.exists(sel):
    os.mkdir(sel)