"""
    날짜 : 2020/06/22
    이름 : 김동욱
    내용 : 딕셔너리 자료형 실습하기 p88
"""

# 딕셔너리 생성
dic1 = {1: 'python', 2: 'java', 3: 'C', 4: 'C++'}
dic2 = {
    'kor': '대한민국',
    'usa': '미국',
    'chi': '중국',
    'jpn': '일본',
    'uk': '영국',
    'tai': '대만'
}
dic3 = {
    101: [1, 2, 3, 4, 5], # 리스트
    102: ('서울', '대전', '대구', '부산', '광주'), # 튜플
    103: {'p1': '김유신', 'p2': '이성계', 'p3': '이순신'} # 딕셔너리
}

# 딕셔너리 값 출력
print('dic1 : ', dic1)
print('dic2 : ', dic2)
print('dic3 : ', dic3)

print('dic1[1] : ', dic1[1]) # []<-키 값
print("dic2['kor'] : ", dic2['kor'])
print("dic3[102] : ", dic3[102])
print("dic3[102][1] : ", dic3[102][1])
print("dic3[103] : ", dic3[103])
print("dic3[103]['p3'] : ", dic3[103]['p3'])

# 딕셔너리 값 제거
del dic1[3]
print('dic1 : ', dic1)

# 딕셔너리 관련 함수 p93~p96
# p93
a = {'name': 'pey', 'phone': '01199933323', 'brith': '1118'}
a.keys()
print(a.keys())

# p94
for k in a.keys():
    print(k)

print(list(a.keys()))

print(a.values())

# p95
print(a.items())

a = {'name': 'pey', 'phone': '01199933323', 'brith': '1118'}
a.get('name')
print(a.get('name'))
a.get('phone')
print(a.get('phone'))

# p96
print(a.get('nokey'))

print(a.get('foo', 'bar'))

a = {'name': 'pey', 'phone': '01199933323', 'brith': '1118'}
print('name' in a)

print('email' in a)