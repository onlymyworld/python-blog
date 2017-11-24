# 导入Mysql驱动
import mysql.connector
# 连接数据库
conn=mysql.connector.connect(user='root',password='123456',database='blog')
# 创建游标
cursor=conn.cursor()
# 创建数据表
cursor.execute('create table comments (id varchar(10),name varchar(20),comments varchar(100))')
# 插入数据
cursor.execute('insert into comments(id,name,comments) values(%s,%s,%s)',[1,'yf','this is comments'])
# 打印出操作数据库影响的行数
print(cursor.rowcount)
# 查询表格中所有数据
cursor.execute('select * from comments')
# 读取出查询的数据并放入values中
values= cursor.fetchall()
# 打印查询出的结果
print(values)
# 提交数据操作的action
cursor.commit()
cursor.close()
conn.close()