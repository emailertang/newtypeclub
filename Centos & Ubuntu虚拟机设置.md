# Centos & Ubuntu虚拟机设置

## 1.安装pip

```shell
#前提是python对应的是Python2 python3对应的是Python3
sudo python get-pip.py
sudo python3 get-pip.py

```

## 2.系统关机和重启

```shell
halt -p -d -i
reboot -f
shutdowm -h now
poweroff
```

## 3.vim

```shell
sudo yum -y install build-essential cmake #编译用

```

4.网络访问设置

```
vim /etc/ssh/sshd_config
注释取消port22
vim /etc/sysconfig/network-srcipts/ifcfg-eth0
修改ONBOOT=yes

```

5.用户设置

```shell
useradd shuoyar
passwd shuoyar
visudo
按上下键找到root    ALL=(ALL)       ALL 这一行内容。
按 i 键进入插入模式，然后输入username ALL=(ALL)  ALL 。
#安装上传工具rz
sudo yum install lrzsz
#安装python依赖环境
yum install gcc-c++ 
yum install -y pcre pcre-devel
yum install -y zlib zlib-devel 
yum install -y openssl openssl-devel
yum install epel-release
yum install -y readline-devel
yum install -y openssl-static
yum groupinstall "Development tools"
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```

