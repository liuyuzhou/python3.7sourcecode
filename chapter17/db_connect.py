#! /usr/bin/python
# -*-coding:UTF-8-*-

import pymysql

def db_connect():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "test")

    # 使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取单条数据
    data = cursor.fetchone()

    print(f"Database version : {data[0]} ")

    # 关闭数据库连接
    db.close()

def main():
    db_connect()

if __name__ == "__main__":
    main()
