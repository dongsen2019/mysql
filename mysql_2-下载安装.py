# 2.下载安装

"""
1.下载mysql5.7.30 官网：mysql.com    window : x86, 64-bit, zip Archive

2.解压安装包,E:\mysql\mysql-5.7.30-winx64


3.在面的路径中新建一个my.ini配置文件，原始的my-default.ini配置文件只是个模板，不要在里面改动
my.ini的内容如下：

课程的配置内容：
[mysql]
default-character-set=utf8

[mysqld]
port=3306
basedir=E:\mysql\mysql-5.7.30-winx64\
datadir=E:\mysql\mysql-5.7.30-winx64\data\
max_connections=200
character-set-server=utf8
default-storage-engine=INNODB
explicit_defaults_for_timestamp=true


百度经验的配置内容：
[mysql]

#设置mysql客户端默认字符集

default-character-set=utf8

[mysqld]

#设置3306端口

port=3306

#设置mysql的安装目录

basedir=E:\mysql-5.7.25

#设置mysql数据库的数据的存放目录

datadir=E:\mysql-5.7.25\data

#允许最大连接数

max_connections=200

# 服务端使用的字符集默认为8比特编码的latin1字符集

character-set-server=utf8

#创建新表时将使用的默认存储引擎

default-storage-engine=INNODB


*****  mysql sql_mode 之 NO_ENGINE_SUBSTITUTION  *****
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
https://www.cnblogs.com/JiangLe/p/5621856.html


4.在安装路径下新建一个空的data文件夹



5.以管理员身份运行cmd，进入bin目录，执行 mysqld --initialize-insecure --user=mysql 命令。
  不进行这一步，安装完成之后无法启动服务


6.依然在管理员cmd窗口的bin目录下，执行 mysql install 命令安装。完成后会提示安装成功。


7.依然在管理员cmd窗口的bin目录下，执行 net start mysql 命令启动mysql服务。

8.修改环境变量，添加 E:\mysql\mysql-5.7.30-winx64\bin

9.在普通cmd窗口中，进入bin目录，执行 mysql -u root -p 命令，默认没有密码，直接回车进入