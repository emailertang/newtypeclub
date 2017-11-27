---

---

# LNMPD（Nginx+Uwsgi+Mysql(Mariadb)+Python&Django）服务器环境配置

## 1.Linux（Centos 6.9）

```bash
su usrname
useradd name
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
 #=======================挂起进程相关===============
 ctrl+Z #挂起进程
 jobs #查看挂起的进程
 fg 进程号 #将挂起的进程放到前台
#====================查看进程的常用格式==========
 ps命令进程查看命令
ps命令：process status
-e 显示所有进程
-f 全格式
-h 不显示标题
-l 长格式
-w 宽输出
a 显示终端上的所有进程，包括其他用户的进程
r 只显示正在运行的进程
x 显示没有控制终端的进程

最常用三个参数是u、a、x。
#ps axu的输出格式
USER：进程拥有者
PID：进程号
%CPU：占用的CPU使用率
%MEM：占用的内存使用率
VSZ；占用的虚拟内存大小
RSS：占用的内存大小
TTY：终端设备号
STAT：改进程状态
START：进程开始时间
TIME：执行的时间
COMMAND：所执行的指令
D:不可中断的休眠（通常表示该进程正在进行I/O动作）
R:正在执行中
S:休眠状态
T:暂停执行
W:没有足够的内存分页可分配
<:高优先顺序的进程
N:低优先顺序的进程
L:有内存分页分配并锁在内存内（即时系统或定制I/O）

Kill:中断一个处理进程(process)
当中断一个前台进程是通常用ctrl+c；对于后台进程用kill命令
kill命令是通过向进程发送指定的信号来结束的。默认为TERM信号。TERM信号将终止所有不能捕获该信号的进程，对于能捕获该信号的进程需要使用kill –9信号，该信号是不能被捕获的。
kill杀终端，只能可以把终端的shell杀死，而退出终端，但终端不关闭
pkill 命令名 可以直接杀死进程
pkill qmail //直接杀死qmail程序进程

```

```bash
#=====================用户设置======================
useradd shuoyar
passwd shuoyar
visudo
按上下键找到root    ALL=(ALL)       ALL 这一行内容。
按 i 键进入插入模式，然后输入username ALL=(ALL)  ALL 。
#==================安装上传工具rz===================
sudo yum install lrzsz
#===========================安装epel==================
rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm # 在package无法找到的情况下执行这个
#=====================安装python依赖环境============
yum install gcc-c++ 
yum install -y pcre pcre-devel
yum install -y zlib zlib-devel 
yum install -y openssl openssl-devel
yum install epel-release
yum install -y readline-devel
yum install -y openssl-static
yum groupinstall "Development tools"
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

#==================网络访问设置=====================
vim /etc/ssh/sshd_config
注释取消port22
vim /etc/sysconfig/network-srcipts/ifcfg-eth0
修改ONBOOT=yes
vim /etc/sysconfig/iptables
#增加两行，打开8000端口，
-A INPUT -m state --state NEW -m tcp -p tcp --dport 8000 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --sport 8000 -j ACCEPT
#====================打开iptables的端口==========
#--dport 8000是进入服务器的端口,--sport是出服务器的数据流端口,还有防火墙的firewall设置,不过除了centos7没有安装
#============================安装locate==============
sudo yum install *locate
sudo updatedb
```



## 2.Python安装

```shell
#安装python2.7和python3

#安装环境 同上
yum install epel-release
yum install -y readline-devel #readline-devel 如果没有安装的话，会造成进入python解释器上下左右回退键都输入不正常。
yum install -y openssl-static
yum install -y openssl-devel&
yum install -y gcc wget 
yum groupinstall "Development tools"
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
#安装setuptools 可以跳过，安装pip会更新
wget https://pypi.python.org/packages/6b/dd/a7de8caeeffab76bacf56972b3f090c12e0ae6932245abbce706690a6436/setuptools-28.3.0.tar.gz
tar xzf setuptools-28.3.0.tar.gz
cd setuptools-28.3.0/
python setup.py install
cd ../
#下载python源码包或者ftp上传
wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tar.xz
tar -xJvf Python-2.7.12.tar.xz
cd Python-2.7.12/
./configure --prefix=/usr/local/python2.7 #安装路径
./configure --prefix=/usr/local/python3
make
make install
#建立链接
mv /usr/bin/python /usr/bin/python.2.6
ln -s /usr/local/python2.7/bin/python2.7 /usr/bin/python #直接使用绝对路径,需要更改yum的python2.6指向
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
#由于系统自带的python路径是/usr/bin/python。PATH中，/usr/local/bin比/usr/bin靠前，所以当你输入python，系统会自动启动你安装的python2.7.12。
echo $PATH
/usr/lib64/qt-3.3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
#!/bin/env python #在python脚本中，你可以使用env来搜寻python
#!/usr/local/bin/python 这样，CentOS7.2调用的也是你安装的2.7.12。好处是当你在别的环境里运行，不需要改第一行也能执行。当然你也可以使用绝对路径：
#修改yum的python
vi /usr/bin/yum
/usr/bin/python 改成 /usr/bin/python2.6

#安装pip3
sudo ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
#安装pip2
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
或者直接下载pip的whl文件
sudo ln -s /usr/local/python2.7/bin/pip /usr/bin/pip

#更改pip源
永久修改： 
linux: 
修改 ~/.pip/pip.conf (没有就创建一个)， 内容如下：

[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
windows: 
直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
#安装virtualenv virtualenvwrapper
```



## 3.virtualenv

```shell
mkdir .virtualenvs
vim .bashrc
export WORKON _HOME=$HOME/.virtualenvs
source /usr/local/python2.7/bin/virtualenvwrapper.sh
workon py2env
source .bashrc #如果找不到 virtualenvwrapper.sh 则自己建立软连接到/usr/local/bin locate virtualenvwrapper.sh updatedb 或者直接更改位置
ln -s /usr/local/python2.7/bin/virtualenv /usr/local/bin

pip install virtualenvwrapper
pip install virtualenvwrapper-win　　#Windows使用该命令
#第一行：virtualenvwrapper存放虚拟环境目录
#第二行：virtrualenvwrapper会安装到python的bin目录下，所以该路径是python安装目录下bin/virtualenvwrapper.sh

#以下内容废弃======================================
1，先yum intall virtualenv
2，然后pip install virtualenvwrapper
安装完需要配置：
[plain] view plain copy
vim ~/.bash_profile  

下面代码添加到后面
Shell Startup File

Add three lines to your shell startup file (.bashrc, .profile, etc.) to set the location where the virtual environments should live, the location of your development project directories, and the location of the script installed with this package:
[plain] view plain copy
#virtualenvwrapper   
export WORKON_HOME=$HOME/virtualenvs # 虚拟环境存放位置自己指定   
source /usr/bin/virtualenvwrapper.sh # 指定virtualenvwrapper的执行文件路径  
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python # 系统python2.7执行文件位置，根据自己环境而定   
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages' # 启动时候指定参数，就是我们用的独立于系统的安装包   
export PIP_VIRTUALENV_BASE=$WORKON_HOME # 告知pip virtualenv的位置   
export PIP_RESPECT_VIRTUALENV=true # 执行pip的时候让系统自动开启虚拟环境   


After editing it, reload the startup file (e.g., run source ~/.bashrc).
执行：
[plain] view plain copy
source ~/.bash_profile  

这里我没理解，我直接在shell里运行这三个命令也是可以的

-------------------------------------------------------------------------------------------------------------------------安装和配置完了

下面是使用：
[plain] view plain copy
mkvirtualenv demo1  
  
workon 切换到环境  
  
deactivate 注销当前环境  
  
lsvirtualenv 列出所有环境  
  
rmvirtualenv 删除环境  
  
cpvirtualenv 复制环境  
  
cdsitepackages cd到当前环境的site-packages目录  
  
lssitepackages 列出当前环境中site-packages内容  
  
setvirtualenvproject 绑定现存的项目和环境  
  
wipeenv 清除环境内所有第三方包  


版权声明：本文为博主原创文章，未经博主允许不得转载
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

下面是mysql的安装

```bash
软件包的管理工具

yum  基于rpm的软件包管理器，可以自动处理依赖关系

    linux上的mysql安装
    
    查看已经安装的mysql文件
    rpm -qa | grep mysql
    
    查看可以按的RPM包
    yum list | grep ^mysql
    
    安装mysql开发包及mysql服务端
    sudo yum install mysql-devel mysql-server
    
    启动mysql：
    sudo service mysqld start
    会出现非常多的信息，目的是对mysql数据库进行初始化操作
    
    
    查看mysql服务是否开机自启动
    chkconfig --list | grep mysqld
    
    如果没有启动，可以通过下面语句来启动：
    sudo chkconfig mysqld on
    
    #通过命令给root账号设置密码为root
    (注意：这个root账号是mysql的root账号，非Linux的root账号)
    mysqladmin -u root password 'root'
    
    通过 mysql -u root -p 命令来登录我们的mysql数据库了
    
    进入mysql后
    查看编码集
    SHOW VARIABLES LIKE '%char%';
    
    查看校对集
    SHOW VARIABLES LIKE '%colla%';
    
    
    改配置文件：
    
    查看服务的状态
    service mysqld status
    关闭服务
    sudo service mysqld stop
    
    
    进入文件
    sudo vi /etc/my.cnf
    
    
    # 往里面加进进去的内容
    # 服务端
    [mysqld]
    character-set-server=utf8
    collation-server=utf8_general_ci
    
    # 客户端：
    [client]
    default-character-set=utf8
    
    重启服务
    sudo service mysqld restart
    



```

rpm安装mysql

```
rpm安装MySQL5.7:

    [budong@budong tools]$ rpm -qa|grep mariadb*    #首先删除已有的mariadb，mysql数据库，
    #使用rpm -e --nodeps mariadb-...   删除安装的数据库
    [budong@budong tools]$ wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.19-1.el6.i686.rpm-bundle.tar
    #即下载群文件进阶软件10，在虚拟机里面下载很慢，大家可以打开这个链接用迅雷去下
    
    [budong@budong tools]$ sudo yum install lrzsz
    #大家从群文件里面下载之后，安装这个，就可以直接从主机拖到虚拟机里面
    
    [budong@budong tools]$ tar -xvf 10mysql-5.7.19-1.el6.i686.rpm-bundle.tar  #解压
    
    [budong@budong tools]$ sudo yum -y install numactl #安装一个依赖
    
    #必须要按照下面的顺序来，不然就会安装不上
    [budong@budong tools]$ sudo rpm -ivh mysql-community-common-5.7.19-1.el6.i686.rpm 
    [budong@budong tools]$ sudo rpm -ivh mysql-community-libs-5.7.19-1.el6.i686.rpm 
    [budong@budong tools]$ sudo rpm -ivh mysql-community-client-5.7.19-1.el6.i686.rpm
    [budong@budong tools]$ sudo rpm -ivh mysql-community-server-5.7.19-1.el6.i686.rpm
    
    #切换root身份，数据库初始化，也可以一开始就切换成root
    [root@budong tools]# mysqld --initialize --user=mysql
    
    #查看root密码  xormlHYlC1&o  就是自己生成的root密码
    [root@budong tools]# cat /var/log/mysqld.log | grep 'password' 
    2017-08-09T12:49:51.364886Z 1 [Note] A temporary password is generated for root@localhost: xormlHYlC1&o  
    
    #启动MySQL服务
    [root@budong tools]# service mysqld start  
    
    #登陆
    [root@budong tools]# mysql -u root -p
    
    #修改 root 密码
    mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'qwe123';
    
    #退出
    mysql> \q
    
    #修改配置文件
    [root@budong tools]# vim /etc/my.cnf
    [mysqld]
    
    datadir=/var/lib/mysql
    socket=/var/lib/mysql/mysql.sock
    character_set_server = utf8
    
    symbolic-links=0
    
    [mysqld_safe]
    log-error=/var/log/mysqld.log
    pid-file=/var/run/mysqld/mysqld.pid
    
    [client]
    default-character-set=utf8
    socket=/var/lib/mysql/mysql.sock
    
    [mysql]
    default-character-set = utf8
    
    #重启服务
    [root@budong tools]# service mysqld restart
    
    #清理安装
    [root@budong tools]# mysql_secure_installation
    此时输入 root 密码，接下来，为了安全，MySQL 会提示你密码为级别，重置 root 密码，移除其他用户账号，禁用 root 远程登录，移除 test 数据库，重新加载 privilege 表格等，你只需输入 y 继续执行即可。如果root密码改啦的话就是输no，其他的地方一直y就可以啦。至此，整个 MySQL 安装完成。
    
    #设置开机启动
    [root@budong tools]# chkconfig --levels 235 mysqld on
    
    #再次登陆MySQL
    [root@budong tools]# mysql -u root -p
    
    #查看字符集
    mysql> SHOW VARIABLES LIKE 'character%';
    
    #创建管理员用户 因为root用户限制不能远程登陆
    mysql> CREATE USER 'admin'@'%' IDENTIFIED BY 'rootqwe123';
    
    #给这个用户授予所有的远程访问的权限。这个用户主要用于管理整个数据库、备份、还原等操作。
    mysql> GRANT ALL  ON *.* TO 'admin'@'%';
    
    #使更改立即生效
    mysql> FLUSH PRIVILEGES;
    
    #创建普通用户
    mysql> CREATE USER 'develop'@'%' IDENTIFIED BY 'QWEqwe123';  #这里的%代表可以远程登陆
    
    #给这个用户授予 SELECT,INSERT,UPDATE,DELETE 的远程访问的权限，这个账号一般用于提供给实施的系统访问
    mysql> GRANT SELECT,INSERT,UPDATE,DELETE  ON *.* TO 'develop'@'%';
    
    #使更改立即生效
    mysql> FLUSH PRIVILEGES;
    
    #退出
    mysql> \q
    
    #以上就是在centos6.9上用rpm安装MySQL5.7.19的方法，注意这个方法适用5.7.5之后的版本



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

