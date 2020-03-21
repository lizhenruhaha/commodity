-- 创建数据库
create database shoparound;

-- 切换数据库
use shoparound;


-- 建表


create table info(
id int primary key auto_increment,
shop_names varchar(200),
prices int(15),
shop_urls varchar(1000),
pic_urls varchar(1000),
search_name varchar(20)
);

show tables;

select * from info;


-- 清空表数据

truncate info;

drop database shoparound;