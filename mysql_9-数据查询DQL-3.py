# Mysql中的统计函数(聚合函数)
"""
max(),min(),count(),sum(),avg()

# 计算 users 表中 最大年龄，最小年龄，年龄及平均年龄
mysql> select max(age),min(age),sum(age),avg(age) from users;
+----------+----------+----------+----------+
| max(age) | min(age) | sum(age) | avg(age) |
+----------+----------+----------+----------+
|      456 |      123 |      579 | 289.5000 |
+----------+----------+----------+----------+

-- 上面数据中的列都是在查询时使用的函数名，不方便阅读和后期调用，可以通过别名方式 美化
mysql> select max(age) as max_age,min(age) as min_age,sum(age) as sum_age,avg(age) as avg_age from users;
+---------+---------+---------+----------+
| max_age | min_age | sum_age | avg_age  |
+---------+---------+---------+----------+
|     456 |     123 |     579 | 289.5000 |
+---------+---------+---------+----------+

-- mysql> select count(*) from user;
+----------+
| count(*) |
+----------+
|        2 |
+----------+

--mysql> select count(age) from user;
+------------+
| count(age) |
+------------+
|          2 |
+------------+

-- 上面的两个统计，分别使用了 count(*)  和 count(id),结果目前都一样，区别是：
count(*) 是按照users表中所有的列进行数据的统计，只要其中一列上有数据，就可以计算
count(age) 是按照指定的 age 字段进行统计，也可以使用别的字段进行统计
但是注意，如果指定的列上出现了NULL值，那么为NULL的这个数据不会被统计
"""
