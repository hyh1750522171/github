# CentOS7 64位安装mysql教程，亲测完美
从最新版本的linux系统开始，默认的是 Mariadb而不是mysql！这里依旧以mysql为例进行展示从最新版本的linux系统开始，默认的是 Mariadb而不是mysql！这里依旧以mysql为例进行展示

一、 先检查系统是否装有mysql
```shell script
rpm -qa | grep mysql
```
这里返回空值，说明没有安装
这里执行安装命令是无效的，因为centos-7默认是Mariadb，所以执行以下命令只是更新Mariadb数据库
```shell script
yum install mysql
```
删除可用
```shell script
yum remove myslq
```
二、 下载`mysql`的`repo`源
```shell script
wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
```
安装`mysql-community-release-el7-5.noarch.rpm`包
```shell script
sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
```
三、安装`mysql`
```shell script
sudo yum install mysql-server
```
根据步骤安装就可以了，不过安装完成后，没有密码，需要重置密码
安装之后再次查看`mysql`
如果报错，内容含有
```shell script
Error: Package: mysql-community-libs-5.6.35-2.el7.x86_64 (mysql56-community)
           Requires: libc.so.6(GLIBC_2.17)(64bit)
Error: Package: mysql-community-server-5.6.35-2.el7.x86_64 (mysql56-community)
           Requires: libc.so.6(GLIBC_2.17)(64bit)
Error: Package: mysql-community-server-5.6.35-2.el7.x86_64 (mysql56-community)
           Requires: systemd
Error: Package: mysql-community-server-5.6.35-2.el7.x86_64 (mysql56-community)
           Requires: libstdc++.so.6(GLIBCXX_3.4.15)(64bit)
Error: Package: mysql-community-client-5.6.35-2.el7.x86_64 (mysql56-community)
           Requires: libc.so.6(GLIBC_2.17)(64bit)
 You could try using --skip-broken to work around the problem
 You could try running: rpm -Va --nofiles --nodigest
```
解决
```shell script
yum install -y glibc.i686
yum list -y libstdc++*
```
四、重置密码
重置密码前，首先要登录
```shell script
myslq -u root

登录时有可能报这样的错:ERROR 2002 (HY000): Can’t connect to local MySQL server through socket ‘/var/lib/mysql/mysql.sock’ (2)，原因是/var/lib/mysql的访问权限问题。下面的命令把/var/lib/mysql的拥有者改为当前用户：
# sudo chown -R openscanner:openscanner /var/lib/mysql
如果报chown: 无效的用户: "openscanner:openscanner"错误，更换命令，并用 ll 查看目录权限列表

chown root /var/lib/mysql/
```