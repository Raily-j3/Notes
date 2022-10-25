# MySQL #


* 表 (类) -> 列: 字段 (属性) 行: (对象)
* my.ini ( MySQL 配置信息)

## 安装和常见命令 ##

```powershell
mysqld --initialize-insecure --user=mysql           # 创建 data 目录
mysqld --install --defaults-file="abs_path\my.ini"  # 创建配置 my.ini
mysql -h localhost -P 3306 -u root -p # exit
set password for root@localhost = password('YourPassword');
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
```
 
```SQL

SHOW DATABASES;                         -- 查看所有数据库
USE dbname;                             -- 进入某个数据库
SHOW TABLES;                            -- 查看库中所有表
SHOW TABLES FROM mysql;                 -- 从所在库查看其他库的所有表
SELECT version();                       -- 查看当前版本
SELECT database();                      -- 所在库
SOURCE sql_name.sql                     -- 导入 sql 文件
ifnull(field, "")

```
## 数据类型 ##

1. 数值类型
    1. 整型：tinyint(1B)、smallint(2B)、mediumint(3B)、int(4B)、bigint(8B)
    2. 小数型：float、double、decimal

2. 字符串类型
    * char( 定长，快，占空间 )、varchar( 变长，慢些，要多长给多大 )、(text)
 
3. 日期类型
    * date日期、time时间、datetime日期时间、year年
    * 时间戳：从 1970-01-01 00:00:00 至指定时间点


## CRUD ##

```sql
CREATE DATABASE d_name charset utf8;            -- 指定编码
SHOW create database d_name;                    -- 查看结构

CREATE TABLE table_name(                        -- 创建表
    value_name type,
    ...
);

CREATE TABLE cp_table_name LIKE table_name;
INSERT INTO cp_table_name SELECT * FROM table_name;

-- CRUD 增查改删
INSERT INTO table_name ([field]) VALUES(        -- C 插入数据
    ...
);
SELECT * FROM table_name WHERE 条件;            -- R
UPDATE table_name SET field1=v WHERE field2=x   -- U
DELETE FROM table_name WHERE 条件;              -- D
DESC/DESCRIBE table_name                        -- 查看表结构

```

### mysql建表约束 ###

1. 自增约束：   auto_increment
2. 唯一键约束： unique 可多个字段
3. 非空约束：   not null
4. 默认约束：   default 10
5. 外键约束：   foreign key(loc) references table(rele)

KEY:  key, primary key, foreign key, unique key

```sql
-- 主键约束：primary key 不能为null 唯一字段
CREATE TABLE user1(
    id int primary key,
    `name` varchar(10),
    -- primary key(id, `name`) 联合主键 id or name 唯一
);

```

### 修改表 ###

```sql
ALTER TABLE table_name RENAME stus;
ALTER TABLE table_name MODIFY id int primary key;                       -- 改字段属性
ALTER TABLE table_name CHANGE column field_name change_name type;       -- 改字段名
ALTER TABLE table_name ADD/DROP primary key(id)/primary key;                        -- 增加，删除字段
ALTER TABLE table_name alter column field_name set default "value";     -- 删除设置默认值速度快
show create table table_name;                                           -- 查看约束名
```


### 事务 ###

```sql
set @@autocommit=0;
begin | start transaction        -- 开启事务
rollback | commit                -- 结束事务

select @@global.tx_isolation;    -- 查看事务级别 5.x global.tx_isolation; 8.0 global.transaction_isolation
-- 事物的隔离性，隔离级别
read uncommitted; -- 读未提交的
read committed;   -- 读已经提交的
repeatable read;  -- 可以重复读
serializable;     -- 串行化
set global transaction isolation level read committed;

-- 脏读 uncommitted
-- 不可重复读 read-committed
-- 幻读 repeatable-read 两个事务同时操作一张表时，一边提交另一边无法读取。
-- 串行化，等待另一个事务commit才能执行（超时）
-- 隔离级别越高，性能越差
```

### 用户 ###

```sql
-- mysql.user
SELECT user();
CREATE USER 'user_name'@'host' IDENTIFIED BY 'passwd';
DROP USER 'user_name'@'host';
SET PASSWORD = PASSWORD('new');
SET PASSWORD FOR USER = PASSWORD('new');
-- 修改 root 密码：
-- 1. 关闭 mysql 服务
-- 2. mysqld --skip-grant-tables
-- 3. 另开cmd：update user set authentication_string=password('123456') where user='root';
-- 4. flush privileges
```

### 权限 ###

* GRANT ALL PRIVILEGES ON *.* TO 'user_name'@'%' IDENTIFIED BY 'passwd';  ( %: 所有主机 )
* REVOKE ALL PRIVILEGES FROM 'username'@'host';

### 简单备份 ###

* mysqldump -u root -p database_name > 备份文件.sql

### 数据编码 ###

* SHOW VARIABLES LIKE 'character_set%';

[别人家的笔记](https://github.com/hjzCy/sql_node/blob/master/mysql/MySQL%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md)

* 可能存在限制：服务端ip和端口绑定，密码规则，防火墙（端口），host权限，用户权限


## MySQL ( bilibili )

- 客户端 ( socket )
- 服务端
- DQL, DML, DDL, TCL, DCL

```sql
-- 一、DQL 查询

-- 执行顺序： from > where > select > group by > having > order by > limit
-- NULL 若参与数据库的运算中,结果必为 NULL
-- ifnull(field, 0) 预处理
-------------------------------------------------------------------
-- 1. 简单查询
select field * 12 as '字段名' from table;  -- 1. 可以运算 2. as(可省略) 别名 3.单引号

-------------------------------------------------------------------
-- 2. 条件查询: <> or !=, beteen...and ...(闭区间); is null, and, or, in, not, like
    -- null 只能 is, is not 判断
    -- 优先级：and or 加括号
    -- field in('value1', 'value2') 等同于 field = 'value1' or field = 'value2'
select field1, field2... from table where condition;

-------------------------------------------------------------------
-- 3. 模糊查询：like %, _
select ename from emp where ename like '%\_%';

-------------------------------------------------------------------
-- 4. 排序：order by asc/desc
select ename, sal from emp order by sal desc, ename asc; -- 字段无法排序时，启用第二个规则

-------------------------------------------------------------------
-- 5. 分组函数：count, sum, avg, max, min ( 只记 5 个
    -- 多行处理函数，对一组数据进行处理
    -- 自动忽略 NULL, 不需添加 where is not null
select count(field) from table; (不为 NULL 的条数)
select count(*) from table; (总记录条数)

-------------------------------------------------------------------
-- 6. 分组：group by 和 having
    -- 当一条语句中有 group by, select 后面只能跟分组函数和参与分组的字段
    -- 尽量使用 where 筛选原始数据, having 筛选经过计算后的数据

-------------------------------------------------------------------
select count(distinct field) from table;
-- 7. 连接查询
    -- 分类：内( 等值/非等值/自连接 )/外连接( 左/右连接 )/全连接
    -- 笛卡尔积 组合匹配，筛选前不会减少次数
    -- 内连接
    inner join...on...where...

-------------------------------------------------------------------
-- 8. 子查询

-------------------------------------------------------------------
-- 9. union 适用场景：需要将两张没有关联的表的查询数据进行合并显示
    -- 列数必须相同
select ename, job from emp where job = 'MANAGER'
union
select enmae, job from emp where job = 'SALEMAN';
类似于
select ename, job from emp where job in('MANAGER', 'SALEMAN');
select ename, job from emp where job = 'MANAGER' or job = 'SALEMAN');

-------------------------------------------------------------------
-- 10. limit: limit start_index length MySQL 特有
select ename, sal from emp order by sal desc limit 0, 5;




## 10 小时

- SQL 只适用于 RDBMS
- SELECT 1, 2
- FROM ...
- JOIN ... ON ...
- WHERE ...
- ORDER BY ...
- GROUP BY ... HAVING ...
- LIMIT

- REGEXP (mysql only)
- 

