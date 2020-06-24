"""
    날짜 : 2020/06/22
    이름 : 김동욱
    내용 : 집합 자료형 실습하기 p97
"""

# 집합 생성하기
set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])

# 집합 출력하기 - 리스트, 튜플 로 변환 후에 출력
ls = list(set1)
tp = tuple(set2)

print('set1 : ', ls)
print('set2 : ', tp)

# 교집합
print('set1과 set2의 교집합 : ', set1 & set2)

# 합집합
print('set1과 set2의 합집합 : ', set1 | set2)

# 차집합
print('set1과 set2의 차집합 : ', set1 - set2)

#집합 관련 함수 p100 ~ p101 실습하기
# p100
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# p101
s1.update([4, 5, 6])
print(s1)

s1 = set([1, 2, 3])
s1.remove(2)
print(s1)