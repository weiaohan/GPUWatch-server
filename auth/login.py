from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    # 表的名字
    __tablename__ = "user"
    # 表的结构
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    number = Column(String(12))
    email = Column(String(64),unique=True)
    pwd = Column(String(32))

    # def __repr__(self):
    #     """定义 repr 让输出更加直观优雅"""
    #     return '<User {}>'.format(self.name)

#engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
engine=create_engine("mysql+mysqlconnector://root:sdxx@rmydcbs@211.83.111.222:3306/gpu-watcher",echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def find_user():
    try:
        user = session.query(User).filter(User.email=="380629654@qq.com").one()
        return user
    except Exception:
        print("not found")
        return -1
    session.close()

if __name__ == "__main__":
    find_user()