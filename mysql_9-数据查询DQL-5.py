# 5.Order by
"""
我们在mysql中使用select的语句查询的数据结果是根据数据在底层文件的结构来排序的，
首先不要依赖默认的排序，另外在需要排序时使用order by对返回的结果进行排序
Asc  升序，默认
desc 降序

-- 按照年龄对结果进行排序，从大到小
select * from users order by age desc;

-- 从小到大排序 asc 默认就是，可以不写
select * from users order by age

-- 也可以按照多个字段进行排序
select * from users order by age,id; # 先按照age进行排序，age相同情况下，按照id进行排序
select * from users order by age,id desc;

Limit 数据分页
limit n 提取n条数据
limit m,n 跳过m条数据，提取n条数据

-- 查询 users 表中的数据
select * from users limit 3;

-- 跳过前4条数据，再取3条数据
select * from users limit 4,3;

-- limit一般应用在数据分页上面
-- 例如每页显示10条数据，第三页的 limit应该怎么写？思考
第一页  limit 0,10
第二页  limit 10,10
第三页  limit 20,10
第四页  limit 30,10

-- 提取 user表中 年龄最大的三个用户数据 怎么查询？
select * from users order by age desc limit 3;

课后练习题
-- 1.统计班级 classid 为2的男女生人数

-- 2.获取每个班级的 平均年龄，并按照平均年龄从大到小排序

-- 3.统计每个班级的人数，按照从大到小排序

-- 4.获取班级人数最多的 班级id信息
"""