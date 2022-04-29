#리스트,슬라이싱
print('='*60)

list = [1,2,3,4]

print(list[0])


#리스트 추가하기
list.append(5)
print(list)

#리스트 요소 제거
del list[0]
print(list)

#리스트 정렬
list3 = [3,6,1,4,5]
list3.sort()
print(list3)

list3.reverse()
print(list3)

#리스트 값 찾기
print(list3.index(1))

#문자열 슬라이싱
str1="안냥하세요"
print(str1[0])
print(str1[1:2])
print(str1[-1])