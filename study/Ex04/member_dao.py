from db import connect as db


def insert_one(**data):
    sql = "INSERT INTO my_member(username,password) VALUES(%(username)s, %(password)s)"
    try:
        db.cursor.execute(sql, data)
    except Exception as e:
        print(e)
        db.conn.rollback()
        return -1
    db.conn.commit()
    return 1


def select_all():
    sql = "SELECT * FROM my_member"
    db.cursor.execute(sql)
    rows = db.cursor.fetchall()
    return rows


def select_one(**data):
    sql = "SELECT * FROM my_member WHERE id = %(id)s"
    db.cursor.execute(sql, data)
    rows = db.cursor.fetchall()
    return rows


def update_one(**data):
    sql = "UPDATE my_member SET username=%(username)s, password =%(password)s WHERE id=%(id)s"
    try:
        db.cursor.execute(sql, data)
    except Exception as e:
        print(e)
        db.conn.rollback()
        return -1
    db.conn.commit()
    return 1


def delete_one(**data):
    sql = "DELETE from my_member WHERE id=%(id)s"
    try:
        db.cursor.execute(sql, data)
    except Exception as e:
        print(e)
        db.conn.rollback()
        return -1
    db.conn.commit()
    return 1
