# 8.DML操作 数据的增删改

"""
数据的DML操作：添加数据，修改数据，删除数据

添加数据：
    格式： insert into 表名(字段列表) values(值列表...);

-- 标准添加(指定所有字段，给定所有值)
mysql> insert into stu(id,name,age,sex,classid) values(1,"zhangsan",20,'m','lamp138');

-- 指定部分字段添加值
mysql> insert into stu(name,class) values('lisi',lamp138)

-- 不指定字段添加值
mysql> insert into stu values(null,'wangwu',21,'w',lamp138)

-- 批量添加值
mysql> insert into stu values
    ->(null,'zhaoliu',21,'w',lamp94),
    ->(null,'aaa',22,'m',lam94),
      ......
    ->(null,'eee',26,)

修改数据
格式：update 表名 set 字段1=值1，字段2=值2，字段n=值n...where 条件

-- 将id为11的age改为35，sex改为m值
mysql-> update stu set age=35,sex='m' where id=11;

-- 将id值12和14的数据sex改为m，classid改为lamp92
mysql-> update stu set classid=lamp92,sex='m' where id=12 or id=14;
mysql-> update stu set classid=lamp92,sex='m' where in(12,14);

删除数据
格式：detele from 表名 [where 条件]

-- 删除stu表中id值为100的数据
mysql-> detele from stu where stu where id=100;

-- 删除stu表中id值为20到30的数据
mysql-> detele from stu where stu where id>=20 and id<=30;

-- 删除stu表中id值为20到30的数据(between)
mysql-> detele from stu where stu where between 20 and 30;

-- 删除stu表中id值大于200的数据
mysql-> detele from stu where stu where id>=200;

"""