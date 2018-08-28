from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''
建立数据库连接，连接方式为：
mysql+pymysql://数据库用户名:密码@数据库地址/数据库名?charset=utf8
pool_size为数据库连接池数
'''
engine = create_engine('mysql+pymysql://root:root@localhost/test?charset=utf8',
                       echo=False, pool_size = 5)
# 建立会话
DBSession = sessionmaker(bind=engine)
session = DBSession()
# 模型声明
Base = declarative_base()


class NLPAnalysis(Base):
    """
    定义一个类对象，一般称为模型
    __tablename__属性对应数据库名
    其余字段属性对应数据库表中各字段的名称和属性
    """
    __tablename__ = 'nlp_analysis'
    id = Column(Integer, primary_key=True)
    question_title = Column(String(200), default=None, doc='问题标题')
    question_answer = Column(String(500), default=None, doc='问题答案')
    fen_ci_result = Column(String(1000), default=None, doc='标题分词结果')

# drop all根据模型用来删除表，该语句慎用，此处为示例而用，一般不建议使用
Base.metadata.drop_all(engine)
# 根据模型用来创建表
Base.metadata.create_all(engine)