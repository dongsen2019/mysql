# 数据库的操作
"""
1.数据库的创建
# 链接mysql数据库后，进入mysql后可以操作数据表

# 1.创建库
create database [if not exists] tlxy default charset=utf8;
-- 1.数据库 tlxy 如果不存在则创建数据库，存在则不创建
-- 2.创建 tlxy 数据库，并设置字符集utf8
-- 3.无特殊情况都要求为utf8或者utf8mb4的字符编码

2.查看数据库
# 1.查看所有库
show databases;

3.打开库/进入库/选择库
# use 库名
use tlxy

4.删除库
***删除有风险，动手需谨慎***
# 删除库，那么库中的所有数据都将在磁盘中删除。
drop database 库名
"""

# 数据表的操作

"""
1.创建表
语法格式：
    create table 表名(字段名,类型,[字段约束]。。。);
# 实例：
create table users(
    -- 创建ID字段，为正整数，不允许为空 主键，自动递增
    id int unsigned not null primary key auto_increment,
    -- 创建存储 名字 的字段，为字符串类型，最大长度 5个字符，不允许为空
    username varchar(5) not null,
    -- 创建存储 密码 的字段，为字符串类型，最大长度5个，不允许为空
    password char(32) not null,
    -- 创建 年龄 字段，不允许为空，默认值为 20
    age tinyint not null default 20
)engine=innodb default charset=utf8;

# 查看表结构
desc users;

# 查看建表语句
show create table users;

创建表的基本原则：
1.表明和字段名 尽可能的符合命名规范，并且最好能够'见名知意'
2.表中数据必须由唯一标识，即主键定义。无特殊情况，主键都为数字并自增即可
3.表中字段所对应的类型设置合理，并限制合理长度
4.表引擎推荐使用innodb，并无特殊情况都要求为utf8或者utf8mb4的字符编码

2.修改表结构
语法格式：alter table 表名 action(更改的选项)
添加字段
    # 语法：alter table 表名 add 添加的字段信息
    -- 在 users 表中 追加 一个 num 字段
    alter table users add num int not null;
    
    -- 在指定字段后面追加字段 在 users 表中 age字段后面 添加一个 Email 字段
    alter table users add email varchar(50) after age;
    
    -- 在指定字段之前添加字段，在 users 表中 Email 字段前面 添加一个 phone
    alter table users add phone char(11) not null after age;
    
    -- 在表的最前面添加一个字段
    alter table users add aa int first;

删除字段
    # 删除字段 alter table 表名 drop 被删除的字段名
    alter table users drop aa;
"""
