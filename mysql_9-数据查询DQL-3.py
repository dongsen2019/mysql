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

"""
