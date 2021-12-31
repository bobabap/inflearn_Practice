# chapter03-03
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀸스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스)
# 클래스안에 정의할 수 있는 특별한(Built-in) 매소드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt
from typing import Collection

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(l_leng1)

# 네임드 튜플 사용

from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# Point(x=1.0, y=5.0) [출력] 레이블이 되어있다
# Point(x=2.5, y=1.5)

# print(pt3.x)
# print(pt4[1])

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2) # key 접근

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(l_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y') 
Point4 = namedtuple('Point', 'x y x class', rename=True) # (기본값)Default = False (class 예약어)

# 출력
print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
p1 = Point1(x=10, y=35) # 이렇게도 가능
p2 = Point2(20, 40) # 이렇게도 가능
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict) # 튜플 언팩킹은 *하나 딕셔너리 언팩킹은 **두개가 붙는다.


print()



print(p1)
print(p2)
print(p3)
# rename 테스트
print(p4) # Point(x=10 인덱스번호[0], y=20, _2=30 인덱스번호[2], _3=40)
print(p5)

# 사용
print(p1[0]+p2[1])
print(p1.x + p2.y)

x, y = p2

print(x, y)

# 네임드 튜플 메소드
temp = [52, 38] # [52, 38, 4] 이렇게 하면 오류

# _make() : 새로운 객체 생성
p4 = Point1._make(temp) # 리스트를 네이드 튜플로 변환하는것이 _make()

print(p4)

# _fields : 필드 네임 확인, key값 조회
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환 : 정렬된 딕셔너리
print("OrderedDict", p1._asdict())
print("OrderedDict", p2._asdict())
print("OrderedDict", p3._asdict())
print("OrderedDict", p4._asdict()) # temp[52, 38]

print()
print()
# 실 사용 실습
# 반 20명, 4개의 반(A,B,C,D)

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split() # 공백을 기준으로 네게를 리스트로 만듦

print(numbers)
print(ranks)

# List Comprehension 지능형 리스트
students = [Classes(rank, numbers) for rank in ranks for number in numbers]

print(len(students))
print(students)

print()
print()
print()

# 추천 한줄로 한번에 위에 아래 방법은 다름
students2 = [Classes(rank, number)
            for rank in 'A B C D'.split()
                for number in [str(n)
                    for n in range(1, 21)]]

print(len(students2))
print(students2)

# 출력 멋있게 한줄씩 nice
for s in students2:
    print(s)











