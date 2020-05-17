# 6.2 Mysql数据表结构修改
"""
语法格式：alter table 表名 change|modify 被修改的字段信息
change：可以修改字段名
modify：不能修改字段名

# 修改表中的 num 字段 类型，使用 modify 不能修改表字段名
alter table users modify age int default 18;

# 修改表中的 age 字段 为 tinyint 并且字段名为 nn
alter table users change age nn tinyint;

***注意：一般情况下，无特殊要求，不要轻易修改表结构***

3.修改表名
# 语法：alter table 原表名 rename as 新表名

4.更改表中的自增的值
# 在常规情况下，auto_increment 默认从1开始继续递增
alter table users auto_increment = 1000;

5.修改表引擎
# 推荐在定义表时，表引擎为 innodb

# 通过查看建表语句获取当前的表引擎
mysql> show create table users\G;
*************************** 1. row ***************************
       Table: users
Create Table: CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(8) NOT NULL,
  `password` char(32) NOT NULL,
  `age` tinyint(4) NOT NULL DEFAULT '20',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.45 sec)

# 直接查看当前表状态信息
mysql> show table status from tlxy where name = 'users'\G;
*************************** 1. row ***************************
           Name: users
         Engine: InnoDB
        Version: 10
     Row_format: Dynamic
           Rows: 0
 Avg_row_length: 0
    Data_length: 16384
Max_data_length: 0
   Index_length: 0
      Data_free: 0
 Auto_increment: 1
    Create_time: 2020-05-17 11:52:47
    Update_time: NULL
     Check_time: NULL
      Collation: utf8_general_ci
       Checksum: NULL
 Create_options:
        Comment:
1 row in set (0.41 sec)

修改表引擎语句
alter table users engine = 'myisam';

6.删除表
drop table 表名;

"""