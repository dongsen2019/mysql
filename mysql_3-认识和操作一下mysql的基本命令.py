# 3.认识和操作mysql的基本命令

# 登录mysql，在终端输入以下命令，进行登录
# mysql -u root -p

"""
C:\Users\Administrator>mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.30 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
"""

# 查看当前mysql中的所有的库。(库==>数据库==>就像文件夹一样，库里面可以存储很多个表)
# show databases;

"""
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.01 sec)
"""

# 选择需要操作的库，打开库
# use mysql;

# 查看当前库中的所有数据表
# show tables;

"""
+---------------------------+
| Tables_in_mysql           |
+---------------------------+
| columns_priv              |
| db                        |
| engine_cost               |
......
| time_zone_name            |
| time_zone_transition      |
| time_zone_transition_type |
| user                      |
+---------------------------+
31 rows in set (0.00 sec)
"""

# 查看表中的数据。--> 查看user表中的所有数据的所有字段
# select * from user;

# 查看 user表中的所有数据的 host 和 user 字段列
# select host,user from user;
"""
+-----------+---------------+
| host      | user          |
+-----------+---------------+
| localhost | mysql.session |
| localhost | mysql.sys     |
| localhost | root          |
+-----------+---------------+

库，表
库就像是文件夹，库中可以有很多歌表
表就像是我们的excel表格文件一样
每个表中都可以存储很多数据

mysql中可以有很多不同的库，库中可以有很多不同的表
表中可以定义不同的列(字段)
表中可以根据结构去存储很多的数据
"""

# 如何创建自己的库？
# create database 库名 default charset=utf8;

"""
创建库：
mysql> create database tlxy default charset=utf8;
-- Query OK, 1 row affected (0.00 sec)

查看所有库：
show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| tlxy               |
+--------------------+
5 rows in set (0.00 sec)

进入库
use tlxy;


"""

# 创建表的语法
"""
# create table 表名(
    字段名 类型 字段约束，
    字段名 类型 字段约束，
    字段名 类型 字段约束
)engine=innodb default charset=utf8;
"""

"""
# 创建用户表
# create table user(
    name varchar(20),
    age int,
    sex char(1)
)engine=innodb default charset=utf8;
-- Query OK, 0 rows affected (0.04 sec)
"""

# 添加一些数据
"""
# insert into user(name,age,sex) values("admin",26,"男");
# -- Query OK, 1 row affected (0.02 sec)

+--------+------+------+
| name   | age  | sex  |
+--------+------+------+
| admin  |   26 | 男   |
| 张三   |   25 | 女   |
+--------+------+------+
2 rows in set (0.00 sec)
"""




