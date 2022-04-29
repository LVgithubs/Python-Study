# python -m pip install pymysql

from email import charset


from db import connect as db


insert_sql = "INSERT INTO my_member(username, password) VALUES(%s ,%s)"
db.cursor.execute(insert_sql, ["love", "1234"])
# 어디선 utf-8은 utf8
