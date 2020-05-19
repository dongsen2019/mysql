# DQL-Mysql数据查询SQL-2
"""
and 和 or 使用时注意

假设要求 查询users表中 年龄为22或者25的女生信息
select * from users where age=22 or age=25 and sex='女';

思考上面的语句能否返回符合条件的数据？
答案：不能

--上面的查询结果并不符合 查询条件的要求
--问题出在sql计算的顺序上，sql会优先处理and条件
--查询年龄为22的，或者年龄为 25 的女生

--如何改造sql符合我们的查询条件？
--使用小括号来关联相同的条件
select * from users where (age=22 or age=25) and sex='女';

Like 子句
我们可以在where条件中使用=,<,>等符合进行条件的过滤，但是当想要查询
是否包含某个字段时如何过滤？
可以使用like语句进行某个字段的模糊搜索，
例如：查询name字段中包含五的数据

-- like 语句  like某个确定的值 和 where name = '王五' 是一样

-- 使用 % 模糊搜索，% 代表任意个任意字符
-- 查询name字段中包含五的
select * from users where name like '%五%';

-- 查询name字段中最后一个字符 为 五 的;
select * from users where name like '%五';

-- 查询name字段中第一个字符 为 王 的;
select * from users where name like '王%';

-- 使用_单个的下划线，表示一个任意字符，使用和%类似

-- 查询表中 name 字段为两个字符的数据
select * from users where name like '__';

-- 查询 name 字段最后为王的两个字符的数据
select * from users where name like '_王'


注意：where子句中的like在使用%或者_进行模拟搜索时，效率不高，使用时注意：
1.尽可能的不去使用%或者
2.如果需要使用，也尽可能不要把通配符放在开头处
"""


