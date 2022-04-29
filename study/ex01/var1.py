# 파이썬 변수 지려향

#부울 T가 대문자가 되어야함



b1 = True

 # 정수
 
n1 = 1

#실수
n2 = 2.2

#문자열

s1 = '문자'

#긴문자열
s2 = '''
안녕하세요
반갑습니다
히히히히히흐흐흐흐

'''


# 문자안에 쌍따음표 추가

s3 = '그는 말했따.. 왈 왈 왈"왈왈왈"라고~~~~~'

print(type(n1))
print(type(n2))
print(type(s1))
print(type(s2))
print(type(s3))
print('='*30)

#문자안에 변수 바인딩 f-str

username = '홍길동'

s4 = f'안녕 내이름은 {username}야'

print(s4)