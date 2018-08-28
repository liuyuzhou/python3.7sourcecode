from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 建立链接
engine = create_engine('mysql+pymysql://root:root@localhost/test?charset=utf8',
                       echo=False, pool_size=5)
# 建立会话
DBSession = sessionmaker(bind=engine)
session = DBSession()
# 模型声明
Base = declarative_base()


class NLPAnalysis(Base):
    __tablename__ = 'nlp_analysis'
    id = Column(Integer, primary_key=True)
    question_title = Column(String(200), default=None, doc='问题标题')
    question_answer = Column(String(500), default=None, doc='问题答案')
    fen_ci_result = Column(String(1000), default=None, doc='标题分词结果')

# drop all根据模型用来删除表，该语句慎用，此处为示例而用，一般不建议使用
Base.metadata.drop_all(engine)
# 根据模型用来创建表
Base.metadata.create_all(engine)


def insert_record(dict_value, table_name=None):
    """
    插入记录方法
    :param dict_value: 字段值字典
    :param table_name: 表名
    :return: None
    """
    if table_name == 'nlp_analysis' and dict_value:
        data = NLPAnalysis(question_title=dict_value['question_title'],
                           question_answer=dict_value['question_answer'],
                           fen_ci_result=dict_value['fen_ci_result'])
        session.add(data)
        session.commit()
        session.close()


def query_record(query_sql):
    """
    记录查询方法
    :param query_sql: 查询语句
    :return: 查询结果
    """
    return session.execute(query_sql)
