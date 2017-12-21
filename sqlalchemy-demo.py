__author__ = "Neil"
__time__ = "2017/12/21 11:40"
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:19971008@localhost:3306/python_test',encoding='utf8', convert_unicode=True)
##  创建DBSession类型:
DBSession = sessionmaker(bind=engine)
#Base.metadata.create_all(engine) #创建表结构 （这里是父类调子类）
#创建session对象:
session = DBSession()

#增
# 创建新User对象:
new_user = User(id='5', name='bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:

#删
user = session.query(User).filter_by(name="bob").first()
session.delete(user)
session.commit()

#改
user = session.query(User).filter_by(name="bob").first()
user.name = "Alice"
session.commit()

#查
user = session.query(User).filter_by(name="bob").first()
print("%s %s" % (user.name, user.password))
session.close()