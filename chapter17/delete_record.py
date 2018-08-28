#! /usr/bin/python
# -*-coding:UTF-8-*-

import pymysql

def delete_record():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 删除语句
    sql = "DELETE FROM EMPLOYEE WHERE AGE > %d" % 22
    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 提交修改
       db.commit()
       print("DELETE SUCCESS.")
    except Exception as ex:
        print(f"DELETE RECORD FAILED.Case:{ex}")
        # 发生错误时回滚
        db.rollback()
    finally:
        # 关闭连接
        db.close()

def main():
    delete_record()

if __name__ == "__main__":
    main()
