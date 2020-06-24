import pymysql

db = pymysql.connect(host="localhost", user="testuser", password="12345", database="testdb")
cursor = db.cursor()
sql = []
sql.append("""SELECT name,age,cls_id FROM students where gender = '男'""")
# 查询所有男生的姓名，年龄，所在班级名称
sql.append("""SELECT name FROM students where cls_id < 4 or is_delete = 0""")
# 查询所有查询编号小于4或没被删除的学生
sql.append("""SELECT * FROM students where name like '黄_'""")
# 查询姓黄并且“名”是一个字的学生
sql.append("""SELECT * FROM students where cls_id = 3 or cls_id = 1""")
# 查询编号是1或3或8的学生
sql.append("""SELECT * FROM students where cls_id > 3 and cls_id < 8""")
# 查询编号为3至8的学生
sql.append("""SELECT * FROM students where gender = '男' and is_delete = 0 order by age desc""")
# 查询未删除男生信息，按年龄降序
sql.append("""SELECT count(gender) FROM students where gender = '女'""")
# 查询女生的总数
sql.append("""SELECT avg(age) FROM students""")
# 查询学生的平均年龄
sql.append("""SELECT gender,avg(age) FROM students where gender = '男' union SELECT gender,avg(age) FROM students where gender = '女'""")
# 分别统计性别为男/女的人年龄平均值
sql.append("""SELECT gender,GROUP_CONCAT(name) from students group by gender""")
# 按照性别来进行人员分组如下显示
for i in sql:
    cursor.execute(i)
    res = cursor.fetchall()
    print(res)
    print()
