# MySQL #

## 名词 ##

* DB (Database 数据库)
* DBMS (DB Management System [MySQL])
  * 两类： 1. 基于文件系统的DBMS ( Access ) 2. 基于C/S ( MySQL.. )
* SQL (Structure Query Language SQL -> DBMS)

* 表 (类) -> 列: 字段 (属性) 行: (对象)
* my.ini ( MySQL 配置信息)
* MySQL 服务的启动停止
* 登陆 MySQL 客户端
  1. 自带客户端( root 用户)
  2. CMD: mysql [-h localhost -P 3306] -u root -p

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

* 数值类型
  1. 整型：tinyint(1B)、smallint(2B)、mediumint(3B)、int(4B)、bigint(8B)
  2. 小数型：float、double、decimal

* 字符串类型
  * char( 定长，快，占空间 )、varchar( 变长，慢些，要多长给多大 )、(text)

* 日期类型
  * date日期、time时间、datetime日期时间、year年
  * 时间戳：从 1970-01-01 00:00:00 至指定时间点

## SQL(DQL, DML, DDL, DCL) ##

### DQL(Data Query Language) ###

### 1.条件查询 ####

```sql
SELECT
    查询列表: ( 字段，常量值，表达式，函数 )
FROM
    表名
WHERE
    筛选条件
SELECT * 着重号 `name` -- 防止重名

-- 起别名
SELECT
    field_name1 AS alias1,
    field_name2 AS alias2,
    field_name3 alias3
FROM
    table_name;

-- 去重
SELECT DISTINCT
    field_name
FROM
    table_name;

-- + 号的作用：数字运算
SELECT 100 + 10;
SELECT "100" + 10;  -- 将字符串转换成数值
SELECT "john" + 10; -- = 10 失败则为 0
SELECT null + 10    -- 结果为 null
SELECT CONCAT('a','b','c') AS 结果; -- IFNULL(field, )

-- 条件查询
-- 100 < x < 200 等价于 100 < x or x < 200
```

### 2.模糊查询 ###

* like + 通配符( 类似正则 )：
   1. % ( 任意 0-n 个字符),
   2. _ ( 任意单个字符 ), 转义 ESCAPE "$", \

* between and:
   1. a <= field <= b, field BETWEEN a AND b

* in:
   1. job_id IN( 'IT_PORT', 'AD_VP', 'AD_PRES' );
   2. is null | is not null

```sql

SELECT
    *
FROM
    employees
WHERE
    last_name LIKE "_$_n_l%" ESCAPE "$";
```

### 3.排序查询 ###

```sql
SELECT
  *
FROM
  table_name
ORDER BY          -- ORDER BY LENGTH(field) DESC/ASC
  field DESC/ASC LIMIT 0,1; -- 默认 ASC limit: 起始位置,长度
```

### 4. 常见函数 ###

1. RAND()   生成随机数
2. COUNT()  个数
3. SUM()    求和
4. AVG()    平均
5. ROUND()  四舍五入

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

### 查询 ###

```sql
-- 分组查询，查询每门课的平均成绩
SELECT AVG(degree) FROM score GROUP BY cno
HAVING count(cno) >= 2;

-- 模糊查询
-- 多表查询
-- 嵌套子查询
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

* mysql.user
* SELECT user();
* CREATE USER 'user_name'@'host' IDENTIFIED BY 'passwd';
* DROP USER 'user_name'@'host';
* SET PASSWORD = PASSWORD('new');
* SET PASSWORD FOR USER = PASSWORD('new');
* 修改 root 密码：
  1. 关闭 mysql 服务
  2. mysqld --skip-grant-tables
  3. 另开cmd：update user set authentication_string=password('123456') where user='root';

### 权限 ###

* GRANT ALL PRIVILEGES ON *.* TO 'user_name'@'%' IDENTIFIED BY 'passwd';  ( %: 所有主机 )
* REVOKE ALL PRIVILEGES FROM 'username'@'host';

### 简单备份 ###

* mysqldump -u root -p database_name > 备份文件.sql

### 数据编码 ###

* SHOW VARIABLES LIKE 'character_set%';

[别人家的笔记](https://github.com/hjzCy/sql_node/blob/master/mysql/MySQL%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md)

* DML
* DDL
  * CREATE, DROP, ALTER, SHOW

* 可能存在限制：服务端ip和端口绑定，密码规则，防火墙（端口），host权限，用户权限
