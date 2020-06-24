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
dic = {'08:00:00': '', '10:10:00': '', '14:00:00': '', '16:10:00': ''}
for i in range(5):
    lis.append(dic)


class Class(Base):
    __tablename__ = "classes"
    name = Column(String(20), primary_key=True)
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
        # conn = pymysql.connect(host='localhost', user='testuser', password='12345', db='class', charset='utf8')
        # cur = conn.cursor()
        # sql = "SELECT * FROM classes"
        # cur.execute(sql)
        # u = cur.fetchall()
        # conn.close()
        env = Environment(loader=FileSystemLoader('C:/Users/asus/Desktop/python/exe11/templates'))
        temp = env.get_template('class.html')
        # temp.render(data=res)
        return render_template('class.html', article=res)
    return render_template('signin.html', message='密码错误', username=username)


if __name__ == '__main__':
    app.run()
