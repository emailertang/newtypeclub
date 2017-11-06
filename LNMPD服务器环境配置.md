---

---

# LNMPD（Nginx+Uwsgi+Mysql(Mariadb)+Python&Django）服务器环境配置

## 1.Linux（Centos 7.4）

```shell
su usrname
usradd name
passwd password
普通用户添加sudo权限
	sudo vim /etc/my.cnf
	username ALL=(ALL)  ALL
cd ../ 定位文件夹
ls  列出文件列表
ln  建立软硬连接
mv 移动文件夹或者改名
mkdir mkdirs 建立文件夹
rmdir 
pwd 显示当前路径
cp 复制
rm -rf 删除文件
touch 建立文件
vi vim 
查找文件
    whereis
    which
    find -path -options
    locate 
    grep
 读取文件信息
 	less
 	more
 	cat
 管道
 	man man | more
echo 输出
linux 目录结构
	~家目录
    /根目录  从逻辑上说系统中的所有一切都隶属于它
    /bin		--存放所有用户都能执行的命令（二制文件）
    /boot		--存放启动文件/内核的相关文件，一般独立成为一个分区。
    /dev		--存放物理设备的目录
    /etc		--存放配置文件
    /home		--用户的家目录
    /lib		--32位库文件
    /lost+found	--分区修复时找回来的文件会存放在这里,
                  存放一些系统不正常关机的的文件残片
    /media		--专门用于挂载的目录
    /misc		--autofs备用文件夹
    /mnt		--专门用于挂载的目录
    /opt		--用于存放第三方软件可选目录
    /proc		--当前内核的映射，一个虚拟的文件系统
    /root		--管理root的家目录
    /sbin		--管理员才能够执行的命令  root
    /selinux	--selinux安全策略相关的文件
    /sys		--内核在内存中的映像文件
    /tmp		--临时目录，建议独立划成分区
    /usr		--用于存放第三方软件
    /var		--存放日志或者频繁修改的文件
 chmod
 shutdown -h now
 reboot
```











## 2.Nginx

```shell
#安装gcc环境用于nginx源码编译
yum install gcc-c++ 
#PCRE(Perl Compatible Regular Expressions) 是一个Perl库，包括 perl 兼容的正则表达式库。nginx 的 http 模块使用 pcre 来解析正则表达式，所以需要在 linux 上安装 pcre 库，pcre-devel 是使用 pcre 开发的一个二次开发库。nginx也需要此库。
yum install -y pcre pcre-devel 
#zlib 库提供了很多种压缩和解压缩的方式， nginx 使用 zlib 对 http 包的内容进行 gzip ，所以需要在 Centos 上安装 zlib 库。
yum install -y zlib zlib-devel 
#OpenSSL 是一个强大的安全套接字层密码库，囊括主要的密码算法、常用的密钥和证书封装管理功能及 SSL 协议，并提供丰富的应用程序供测试或其它目的使用。
yum install -y openssl openssl-devel
#下载nginx 并编译安装
cd /usr/local
wget -c https://nginx.org/download/nginx-1.10.1.tar.gz
tar -zxvf nginx-1.10.1.tar.gz
cd nginx-1.10.1
./configure
#自定义配置
#./configure \
--prefix=/usr/local/nginx \
--conf-path=/usr/local/nginx/conf/nginx.conf \
--pid-path=/usr/local/nginx/conf/nginx.pid \
--lock-path=/var/lock/nginx.lock \
--error-log-path=/var/log/nginx/error.log \
--http-log-path=/var/log/nginx/access.log \
--with-http_gzip_static_module \
--http-client-body-temp-path=/var/temp/nginx/client \
--http-proxy-temp-path=/var/temp/nginx/proxy \
--http-fastcgi-temp-path=/var/temp/nginx/fastcgi \
--http-uwsgi-temp-path=/var/temp/nginx/uwsgi \
--http-scgi-temp-path=/var/temp/nginx/scgi
make
make install
#启动nginx
whereis nginx
cd pathto nginx#/usr/local/nginx/sbin/
./nginx 
./nginx -s stop #杀进程
./nginx -s quit #停止
./nginx -s reload #重启
ps aux|grep nginx #查询进程
./nginx -s quit
./nginx        #重启
./nginx -s reload
#创建自启动
vi /etc/rc.local #增加一行/usr/local/nginx/sbin/nginx
chmod 755 rc.local
```

http://www.linuxidc.com/Linux/2016-09/134907.htm

### Ngnix.conf

```nginx
#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

	server {

			listen   80;
			server_name www.shuoyarnova.top;
			access_log /home/webshop/logs/access.log;
			error_log /home/webshop/logs/error.log;

			#charset koi8-r;

			#access_log  logs/host.access.log  main;

			location / {
			 include        uwsgi_params;
			 uwsgi_pass     127.0.0.1:9090;
			}

			#error_page  404              /404.html;

			# redirect server error pages to the static page /50x.html
			#
			error_page   500 502 503 504  /50x.html;
			location = /50x.html {
				root   html;
			}

			location /static/ {
				alias  /home/webshop/shuoyar/static/;
				index  index.html index.htm;
			}

			location /media/ {
				alias  /home/webshop/shuoyar/media/;
			}
		}

    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}
```



## 4.Python

```shell
rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm # 在package无法找到的情况下执行这个
yum install epel-release
#安装环境
yum install -y readline-devel #readline-devel 如果没有安装的话，会造成进入python解释器上下左右回退键都输入不正常。
yum install -y openssl-static
yum install -y openssl-devel&
yum install -y gcc wget 
yum groupinstall "Development tools"
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
#安装setuptools
wget https://pypi.python.org/packages/6b/dd/a7de8caeeffab76bacf56972b3f090c12e0ae6932245abbce706690a6436/setuptools-28.3.0.tar.gz
tar xzf setuptools-28.3.0.tar.gz
cd setuptools-28.3.0/
python setup.py install
cd ../
#下载python源码包或者ftp上传
wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tar.xz
tar -xJvf Python-2.7.12.tar.xz
cd Python-2.7.12/
./configure --prefix=/usr/local/python2.7
./configure --prefix=/usr/local/python3
make
make install
#建立链接
ln -s /usr/local/python2.7/bin/python2.7 /usr/local/bin/python #由于系统自带的python路径是/usr/bin/python。PATH中，/usr/local/bin比/usr/bin靠前，所以当你输入python，系统会自动启动你安装的python2.7.12。
echo $PATH
/usr/lib64/qt-3.3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
#!/bin/env python #在python脚本中，你可以使用env来搜寻python
#!/usr/local/bin/python 这样，CentOS7.2调用的也是你安装的2.7.12。好处是当你在别的环境里运行，不需要改第一行也能执行。当然你也可以使用绝对路径：
```





## 5.Mysql（Mariadb）

```mysql
yum -y install mariadb mariadb-server #
systemctl start mariadb #安装完成MariaDB，首先启动MariaDB
systemctl enable mariadb #设置开机启动
mysql_secure_installation #安全设置
Enter current password for root (enter for none):<–初次运行直接回车
#设置密码
Set root password? [Y/n] <– #是否设置root用户密码，输入y并回车或直接回车
New password: <– #设置root用户的密码
Re-enter new password: <– #再输入一次你设置的密码
#其他配置
Remove anonymous users? [Y/n] <– #是否删除匿名用户，回车
Disallow root login remotely? [Y/n] <–#是否禁止root远程登录,回车,
Remove test database and access to it? [Y/n] <– #是否删除test数据库，回车
Reload privilege tables now? [Y/n] <– #是否重新加载权限表，回车
#初始化MariaDB完成，接下来测试登录
mysql -uroot -ppassword
#配置字符集
vi /etc/my.cnf
#在[mysqld]标签下添加
init_connect='SET collation_connection = utf8_unicode_ci' 
init_connect='SET NAMES utf8' 
character-set-server=utf8 
collation-server=utf8_unicode_ci 
skip-character-set-client-handshake
-------------------------------------------------------------
vi /etc/my.cnf.d/client.cnf
#在[client]中添加
default-character-set=utf8
#文件/etc/my.cnf.d/mysql-clients.cnf
vi /etc/my.cnf.d/mysql-clients.cnf
#在[mysql]中添加
default-character-set=utf8
#全部配置完成，重启mariadb
systemctl restart mariadb
#之后进入MariaDB查看字符集
mysql> show variables like "%character%";show variables like "%collation%";
显示为
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client    | utf8                      |
| character_set_connection | utf8                      |
| character_set_database  | utf8                      |
| character_set_filesystem | binary                    |
| character_set_results    | utf8                      |
| character_set_server    | utf8                      |
| character_set_system    | utf8                      |
| character_sets_dir      | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.00 sec)

+----------------------+-----------------+
| Variable_name        | Value          |
+----------------------+-----------------+
| collation_connection | utf8_unicode_ci |
| collation_database  | utf8_unicode_ci |
| collation_server    | utf8_unicode_ci |
+----------------------+-----------------+
3 rows in set (0.00 sec)
#字符集配置完成。
#添加用户，设置权限
#创建用户命令
mysql>create user username@localhost identified by 'password';
#直接创建用户并授权的命令
mysql>grant all on *.* to username@localhost indentified by 'password';
#授予外网登陆权限 
mysql>grant all privileges on *.* to username@'%' identified by 'password';
#授予权限并且可以授权
mysql>grant all privileges on *.* to username@'hostname' identified by 'password' with grant option;
#简单的用户和权限配置基本就这样了。
#其中只授予部分权限把 其中 all privileges或者all改为select,insert,update,delete,create,drop,index,alter,grant,references,reload,shutdown,process,file其中一部分。
```



Linux系统教程：如何检查MariaDB服务端版本  <http://www.linuxidc.com/Linux/2015-08/122382.htm>

MariaDB Proxy读写分离的实现 <http://www.linuxidc.com/Linux/2014-05/101306.htm>

Linux下编译安装配置MariaDB数据库的方法 <http://www.linuxidc.com/Linux/2014-11/109049.htm>

CentOS系统使用yum安装MariaDB数据库 <http://www.linuxidc.com/Linux/2014-11/109048.htm>

安装MariaDB与MySQL并存 <http://www.linuxidc.com/Linux/2014-11/109047.htm>

[Ubuntu](http://www.linuxidc.com/topicnews.aspx?tid=2) 上如何将 MySQL 5.5 数据库迁移到 MariaDB 10  <http://www.linuxidc.com/Linux/2014-11/109471.htm>

**[翻译]Ubuntu 14.04 (Trusty) Server 安装 MariaDB**  <http://www.linuxidc.com/Linux/2014-12/110048htm>

**MariaDB 的详细介绍**：[请点这里](http://www.linuxidc.com/Linux/2012-03/56857.htm)
**MariaDB 的下载地址**：[请点这里](http://www.linuxidc.com/down.aspx?id=363)

更多CentOS相关信息见[CentOS](http://www.linuxidc.com/topicnews.aspx?tid=14) 专题页面 <http://www.linuxidc.com/topicnews.aspx?tid=14>

**本文永久更新链接地址**：<http://www.linuxidc.com/Linux/2016-03/128880.htm>

## 6.uwsgi

```shell
pip install uwsgi & curl http://uwsgi.it/install | bash -s default /tmp/uwsgi
wget https://projects.unbit.it/downloads/uwsgi-latest.tar.gz
tar zxvf uwsgi-latest.tar.gz
cd <dir>
make
make install
#测试 uwsgi 是否正常：
#新建 test.py 文件，内容如下：
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return "Hello World"
#然后在终端运行：
#uwsgi --http :8001 --wsgi-file test.py
#在浏览器内输入：http://127.0.0.1:8001，查看是否有"Hello World"输出，若没有输#出，请检查你的安装过程。

-----------------------------------------------------------------------
uwsgi支持ini、xml等多种配置方式，本文以 ini 为例， 在/ect/目录下新建uwsgi9090.ini，添加如下配置：
[uwsgi]
socket = 127.0.0.1:9090
master = true         //主进程
vhost = true          //多站模式
no-site = true        //多站模式时不设置入口模块和文件
workers = 2           //子进程数
reload-mercy = 10     
vacuum = true         //退出、重启时清理文件
max-requests = 1000   
limit-as = 512
buffer-size = 30000
pidfile = /var/run/uwsgi9090.pid    //pid文件，用于下面的脚本启动、停止该进程
daemonize = /website/uwsgi9090.log


#killall -s INT /usr/bin/uwsgi 杀死uwsgi
```

### uwsgi.ini

```ini
# mysite_uwsgi.ini file
[uwsgi]

# Django-related settings
# the base directory (full path)
socket = 127.0.0.1:9090
chdir           = /home/shuoyar/webshop
# Django's wsgi file
module          = webshop.wsgi
# the virtualenv (full path)
#home            = /path/to/virtualenv

# process-related settings
# master
master          = true
# maximum number of worker processes
processes       = 4
# the socket (use the full path to be safe
#socket          = /path/to/your/project/mysite.sock
# ... with appropriate permissions - may be needed
# chmod-socket    = 664
# clear environment on exit
vacuum          = true
```



## 7.Django

```shell
pip install django
#测试 django 是否正常，运行：
#django-admin.py startproject demosite
cd demosite
python2.7 manage.py runserver 0.0.0.0:8002
#在浏览器内输入：http://127.0.0.1:8002，检查django是否运行正常。

```





## 8.python3的问题

```
安装python3.6可能使用的依赖
# yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel

下载python3.6编译安装
到python官网下载https://www.python.org
下载最新版源码，使用make altinstall，如果使用make install，在系统中将会有两个不同版本的Python在/usr/bin/目录中。这将会导致很多问题，而且不好处理。
# wgethttps://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz
# tar -xzvf Python-3.6.0.tgz -C  /tmp
# cd  /tmp/Python-3.6.0/
把Python3.6安装到 /usr/local 目录
# ./configure --prefix=/usr/local
# make
# make altinstall

python3.6程序的执行文件：/usr/local/bin/python3.6
python3.6应用程序目录：/usr/local/lib/python3.6
pip3的执行文件：/usr/local/bin/pip3.6
pyenv3的执行文件：/usr/local/bin/pyenv-3.6

更改/usr/bin/python链接
# cd/usr/bin
# mv  python python.backup
# ln -s /usr/local/bin/python3.6 /usr/bin/python
# ln -s /usr/local/bin/python3.6 /usr/bin/python3

更改yum脚本的python依赖
# cd /usr/bin
# ls yum*
yum yum-config-manager yum-debug-restore yum-groups-manager
yum-builddep yum-debug-dump yumdownloader
更改以上文件头为
#!/usr/bin/python 改为 #!/usr/bin/python2

修改gnome-tweak-tool配置文件
# vi /usr/bin/gnome-tweak-tool
#!/usr/bin/python 改为 #!/usr/bin/python2

修改urlgrabber配置文件
# vi /usr/libexec/urlgrabber-ext-down
#!/usr/bin/python 改为 #!/usr/bin/python2
```

