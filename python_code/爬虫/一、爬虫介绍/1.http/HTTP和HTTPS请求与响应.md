# HTTP和HTTPS

HTTP协议（超文本传输协议）：是一种发布和接收HTML页面方法。

HTTPS（安全套接字层上的超文本传输协议）简单讲就是HTTP的安全版，在HTTP下加入SSL层。

SSL（安全套接字层安全套接层）只要用于Web的安全传输协议，在传输层对网络链接进行加密，保障Internet上数据的安全。
* `HTTP`的端口号为`80`
* `HTTPS`的端口号为`443`
#### HTTP工作原理

网络爬虫抓取过程可以理解为`模拟浏览器操作的过程`。

浏览器的主要功能是向服务器发出请求，在浏览器窗口中展示您选择的网络资源，HTTP是一套计算机通过网络进行通信的规则。
## HTTP的请求与响应
HTTP通信是由两部分组成：`客户端请求消息`与`服务器响应消息`

![](./image/02_http_pro.jpg)
### 浏览器发送HTTP请求的过程
1. 当用户在浏览器的地址栏中输入一个URL并按回车键之后，浏览器会向HTTP服务器发送HTTP请求。HTTP请求主要分为“Get”和“Post”两种方法
2. 当我们在浏览器输入URL http://www.baidu.com 的时候，浏览器发送一个Request请求去获取 http://www.baidu.com 的html文件，服务器把Response文件对象发送回给浏览器。
3. 浏览器分析Response中的 HTML，发现其中引用了很多其他文件，比如Images文件，CSS文件，JS文件。 浏览器会自动再次发送Request去获取图片，CSS文件，或者JS文件。
4. 当所有的文件都下载成功后，网页会根据HTML语法结构，完整的显示出来了。

URL（Uniform / Universal Resource Locator的缩写）：统一资源定位符，是用于完整地描述Internet上网页和其他资源的地址的一种标识方法。

![](./image/01-httpstruct.jpg)

基本格式：`scheme://host[:port#]/path/…/[?query-string][#anchor]`
* scheme：协议(例如：http, https, ftp)
* port#：服务器的端口（如果是走协议默认端口，缺省端口80）
* path：访问资源的路径
* query-string：参数，发送给http服务器的数据
* anchor：锚（跳转到网页的指定锚点位置）

例如：
* ftp://192.168.0.116:8080/index
* http://www.baidu.com
* http://item.jd.com/11936238.html#product-detail
## 客户端HTTP请求
URL只是标识资源的位置，而HTTP是用来提交和获取资源。客户端发送一个HTTP请求到服务器的请求消息，包括以下格式：

`请求行`、`请求头部`、`空行`、`请求数据`

四个部分组成，下图给出了请求报文的一般格式。
![](./image/01_request.png)
*一个典型的HTTP请求示例*
```haml
GET https://www.baidu.com/ HTTP/1.1
Host: www.baidu.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: http://www.baidu.com/
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
Cookie: BAIDUID=04E4001F34EA74AD4601512DD3C41A7B:FG=1; BIDUPSID=04E4001F34EA74AD4601512DD3C41A7B; PSTM=1470329258; MCITY=-343%3A340%3A; BDUSS=nF0MVFiMTVLcUh-Q2MxQ0M3STZGQUZ4N2hBa1FFRkIzUDI3QlBCZjg5cFdOd1pZQVFBQUFBJCQAAAAAAAAAAAEAAADpLvgG0KGyvLrcyfrG-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFaq3ldWqt5XN; H_PS_PSSID=1447_18240_21105_21386_21454_21409_21554; BD_UPN=12314753; sug=3; sugstore=0; ORIGIN=0; bdime=0; H_PS_645EC=7e2ad3QHl181NSPbFbd7PRUCE1LlufzxrcFmwYin0E6b%2BW8bbTMKHZbDP0g; BDSVRTM=0
```

