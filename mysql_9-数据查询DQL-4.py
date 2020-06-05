# Group By 分组

"""
group by 语句根据一个或多个列对结果进行分组
一般情况下，是用与数据的统计或计算，配合聚合函数使用

-- 统计 user 表中 男女生人数
-- 很明显按照上面的需要，可以写出两个语句进行分别统计
select count(*) from users where sex = '女';
select count(*) from users where sex = '男';
-- 可以使用分组进行统计，更方便
mysql> select sex,count(*) from user group by sex;
+------+----------+
| sex  | count(*) |
+------+----------+
| 女   |        2 |
| 男   |        1 |
+------+----------+
"""

