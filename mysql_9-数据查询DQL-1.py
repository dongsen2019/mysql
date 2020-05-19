# DQL-Mysql数据查询SQL-1

"""
语法格式：
    select 字段列表|* from 表名
    where 搜索条件
    group by 分组字段 [having 分组条件]
    order by 排序字段 排序规则
    limit 分页参数

基础查询:

查询表中所有列 所有数据
select * from users;

指定字段列表进行查询
select id,name,phone from users;

Where 条件查询

1.可以在where子句中指定任何条件
2.可以使用and 或者 or 指定一个或多个条件
3.where条件也可以运用在update和delete语句的后面
4.where子句类似程序语言中if条件，根据mysql表中的字段值来进行数据的过滤

示例：
-- 查询 users 表中 age>22 的数据
select * from users where age>22;

-- 查询 users 表中 name=某个条件值 的数据
select * from users where name = '王五';

-- 查询 users 表中年龄在22到25之间的数据
select * from users where age>=22 and age<=25;
select * from users where age between 22 and 25;

-- 查询 users 表中年龄在22到25之间的女生信息
select * from users where (age>=22 and age<=25) and sex='女';
"""