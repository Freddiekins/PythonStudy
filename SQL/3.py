import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, Date
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+mysqlconnector://testuser:12345@localhost:3306/testdb')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Message(Base):
    __tablename__ = "message"
    name = Column(String(20), primary_key=True)
    text = Column(String(255), nullable=False)
    time = Column(Date, nullable=False)
    is_delete = Column(Integer, nullable=False)


session = Session()
msg1 = Message(name='Jack',text='hello',time='2020-05-18',is_delete=0)
msg2 = Message(name='Tom',text='thanks',time='2020-05-30',is_delete=0)
session.add(msg1)
session.add(msg2)
target = session.query(Message).filter(Message.name == "Jack").first()
target.is_delete = 1
res = session.query(Message).filter(Message.is_delete == 1).all()
for i in res:
    session.delete(i)
session.commit()
print(session.query(Message).all())
