import pymysql

db = pymysql.connect(host="localhost", user="testuser", password="12345", database="testdb")
cursor = db.cursor()
sql1 = """insert into message values('Jack','hello','2020-05-18',0)"""
sql2 = """insert into message values('Tom','thanks','2020-05-30',0)"""
sql3 = """update message set is_delete = 1 where name = 'Jack'"""
sql4 = """delete from message where is_delete = 1"""
sql5 = """select * from message"""
cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql5)
res1 = cursor.fetchall()
print(res1)
cursor.execute(sql4)
cursor.execute(sql5)
res2 = cursor.fetchall()
print(res2)
