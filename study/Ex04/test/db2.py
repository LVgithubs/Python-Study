from unittest import result
import member_dao as dao


def setData():
    result = dao.insert_one(username="hong", password="1234")
    print(f"result : {result}")


def getDatas():
    my_members_entity = dao.select_all()
    print(my_members_entity)


def getData():
    my_members_entity = dao.select_one(id=1)
    print(my_members_entity)

# 한건 업데이트하기


def updateData():
    result = dao.update_one(id=1, username="abcd", password="5555")
    print(f"result : {result}")


def deleteData():
    result = dao.delete_one(id=1)
    print(f"result : {result}")
