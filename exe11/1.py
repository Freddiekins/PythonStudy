# 开发设计一个简单的基于web的选课系统（基于flask框架）；学生登陆后，能看到课程列表，
# 点击可以选择该课程（要检查是否和其它已经选择的课程有时间冲突）；
# 自己设计数据库，注意表和字段命名的规范性，数据类型选择的合理性；
from flask import Flask
from flask import request
from flask import render_template
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Time
from sqlalchemy.orm import sessionmaker
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)
engine = sqlalchemy.create_engine('mysql+mysqlconnector://testuser:12345@localhost:3306/class')
Session = sessionmaker(bind=engine)
Base = declarative_base()
lis = []
dic1 = {'08:00:00': '无', '10:10:00': '无', '14:00:00': '无', '16:10:00': '无'}
dic2 = {'08:00:00': '无', '10:10:00': '无', '14:00:00': '无', '16:10:00': '无'}
dic3 = {'08:00:00': '无', '10:10:00': '无', '14:00:00': '无', '16:10:00': '无'}
dic4 = {'08:00:00': '无', '10:10:00': '无', '14:00:00': '无', '16:10:00': '无'}
dic5 = {'08:00:00': '无', '10:10:00': '无', '14:00:00': '无', '16:10:00': '无'}
lis.append(dic1)
lis.append(dic2)
lis.append(dic3)
lis.append(dic4)
lis.append(dic5)


class Class(Base):
    __tablename__ = "classes"
    num = Column(String(10), primary_key=True)
    name = Column(String(10), nullable=False)
    date = Column(String(5), nullable=False)
    time = Column(Time, nullable=False)
    is_selected = Column(String(5), nullable=False)


session = Session()
res = session.query(Class).all()


@app.route('/', methods=['GET'])
def signin_form():
    return render_template('signin.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == '001' and password == '12345':
        env = Environment(loader=FileSystemLoader('C:/Users/asus/Desktop/python/exe11/templates'))
        temp = env.get_template('class.html')
        return render_template('class.html', article=res)
    return render_template('signin.html', message='密码错误', username=username)


@app.route('/class', methods=['POST'])
def choose():
    num = request.form.get('cls_num')
    print(num)
    sql = """SELECT * FROM classes where num = '""" + num + """'"""
    cursor = session.execute(sql)
    re = cursor.fetchall()
    if re and re[0][4] == '否':
        nam = re[0][1]
        dat = re[0][2]
        if str(re[0][3]) == '8:00:00':
            tim = '0' + str(re[0][3])
        else:
            tim = str(re[0][3])
        print(nam, dat, tim)
        print(lis[2][tim])
        if dat == '星期一' and lis[0][tim] == '无':
            lis[0][tim] = nam
        elif dat == '星期二' and lis[1][tim] == '无':
            lis[1][tim] = nam
        elif dat == '星期三' and lis[2][tim] == '无':
            lis[2][tim] = nam
        elif dat == '星期四' and lis[3][tim] == '无':
            lis[3][tim] = nam
        elif dat == '星期五' and lis[4][tim] == '无':
            lis[4][tim] = nam
        else:
            res = session.query(Class).all()
            return render_template('class.html', article=res, msg='与其他课程时间冲突')
        target = session.query(Class).filter(Class.num == num).first()
        target.is_selected = '是'
        session.commit()
        res = session.query(Class).all()
        return render_template('class.html', article=res)
    elif re[0][4] == '是':
        res = session.query(Class).all()
        return render_template('class.html', article=res, msg='课程已选')


if __name__ == '__main__':
    app.run()
