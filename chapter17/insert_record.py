#! /usr/bin/python
# -*-coding:UTF-8-*-

import pymysql
import datetime

def insert_record():
    db = pymysql.connect("localhost", "root", "root", "test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME," \
          " CREATE_TIME) VALUES('%s', '%s', %d, '%c', %d, '%s')" \
          % ('xiao', 'zhi', 22, 'M', 30000, datetime.datetime.now())
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       db.commit()
       print("INSERT SUCCESS.")
    except Exception as ex:
       print(f'INSERT INTO MySQL table failed.Case:{ex}')
       # 如果发生错误就回滚
       db.rollback()
    finally:
        # 关闭数据库连接
        db.close()

def main():
    insert_record()

if __name__ == "__main__":
    main()
