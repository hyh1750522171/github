#hadoop搭建教程
## 所需要的软件以及服务
1. jdk_1.8
2. hadoop_2.6.0
3. centos7.4
4. VMware Workstation Pro 
## 开始安装系统
此过程不在赘述

## 开始配置环境
一、 配置网卡信息
```bash
# vim /etc/sysconfig/network-scripts/对应自己的网卡
ONBOOT=yes
IPADDR=IP
PREFIX=子网掩码位数
GATEWAY=网关
DNS=域名解析服务器ip
```
二、主机名称配置和主机名映射
```haml
vim /etc/hostname
# 文件里面输入你想配置的主机名
这里以node-1为例
node-1
# vim /etc/hosts
添加以下内容
10.10.10.11 node-1
10.10.10.12 node-2
10.10.10.13 node-3
10.10.10.14 node-4
```
三、配置ssh免密登录
```haml
ssh-keygen -t rsa
ssh-copy-id 对方主机名
```
四、配置SElinu防火墙
```shell script
 firewall-cmd --state #查看状态
 systemctl stop firewalld.service # 关闭防火墙
 systemctl disable firewalld.service # 永久关闭防火墙
```
五、配置java环境
```shell script
rpm -qa|grep java # 检查已安装java 然后卸载自带的java
rem -e --nodeps # 检查出来的名称
vim /etc/profile
export JAVA_HOME=/hadoop/java/jdk(java路径可用which java 查询)
export PATH=$PATH:$JAVA_HOME/bin
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
source /etc/profile # 立马生效
# 检查java 版本
java -version
```

