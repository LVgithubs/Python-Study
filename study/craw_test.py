from urllib import response
from pymysql import connect, cursors

conn = connect(
    host="localhost",
    user="green",
    password="green1234",
    db="greendb",
    charset="utf8"
)
cursor = conn.cursor(cursors.DictCursor)  # 기본 tuple

#insert_sql = "INSERT INTO userpy(username, password) VALUES(%s, %s)"
#cursor.execute(insert_sql, ["love", "1234"])
#conn.commit()


# 데이터 다운로드
# python -m pip install requests 라이브러리 다운로드
# Scripts 폴더 환경변수 잡으면 pip부터 할 수 있음

import requests
from bs4 import BeautifulSoup


# response = requests.get("https://data.seoul.go.kr/dataList/OA-2219/S/1/datasetView.do")

html = requests.get("https://data.seoul.go.kr/dataList/OA-2219/S/1/datasetView.do")
#response = requests.get("https://data.seoul.go.kr/dataList/OA-2219/S/1/datasetView.do")
soup = BeautifulSoup(html.text, 'html.parser')


# let weather_el = document.querySelector(".wrap-cont")
# console.log(weather_el)
weather_el = soup.select_one(".AXGridBody")
print(weather_el)



# print(response)  # 헤더에 있는 status 상태코드
# print(type(response))  # 클래스 타입

# dict 검색 : response["키값"]
# class 검색 : response.객체연결
#print(response.text)  # 데이터를 문자열 그대로 읽음(통신 데이터)
# print(type(response.text))  # str 타입
# print(response.json())
# print(type(response.json()))  # dict 타입

# datas = html.json()["response"]["body"]["items"]["item"]
#for data in datas:
#    print(data[""])