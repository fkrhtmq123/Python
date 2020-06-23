"""
    날짜 : 2020/06/23
    이름 : 김동욱
    내용 : for문 p138
"""

# for
# 리스트를 이용한 for
nums = [1, 2, 3, 4, 5]

for n in nums:
    print('n :', n)

for a in ['tiger', 'lion', 'eagle', 'bear']:
    print('a :', a)

# 튜플 이용한 for
for n in (1, 2, 3, 4, 5):
    print('n :', n)

# range 함수를 이용한 for
for num in range(5):
    print('num :', num)
for v in range(1, 10):
    print('v :', v)

# 1부터 10까지 합
sum = 0

for k in range(1, 11):
    sum += k
print('1부터 10까지 합 :', sum)

# 1부터 10까지 짝수 합
tot = 0

for k in range(1, 11):
    if k%2 == 0:
        tot += k
print('1부터 10까지 짝수 합 :', tot)

# 이중 for문
for a in range(0, 3):
    print('a :', a)
    for b in range(0, 5):
        print('b :', b)

# 구구단
for a in range(2, 10):
    print(a, '단 출력')
    for b in range(1, 10):
        print(a, ' X ', b, ' = ', a * b)
        """print('%d x %d = %d' % (a, b, a*b)"""

# 별삼각형
for a in range(0, 10):
    for b in range(1, a+1):
        print('☆', end='')
    print()

for n in range(1, 11):
    print('★'*n)

for a in range(11, 1, -1):
    print('★'*a)

# 별 피라미드 해보기