#! /usr/bin/python
# -*-coding:UTF-8-*-

import pymysql

def query_data():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %d" % 10000
    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 获取所有记录列表
       results = cursor.fetchall()
       for row in results:
          first_name = row[0]
          last_name = row[1]
          age = row[2]
          sex = row[3]
          income = row[4]
          create_time = row[5]
          # 输出结果
          print(f"first_name={first_name},last_name={last_name},age={age},"
                f"sex={sex},income={income},create_time={create_time}")
    except Exception as ex:
       print(f"Error: unable to fecth data.Error info:{ex}")
    finally:
        # 关闭数据库连接
        db.close()

def main():
    query_data()

if __name__ == "__main__":
    main()
