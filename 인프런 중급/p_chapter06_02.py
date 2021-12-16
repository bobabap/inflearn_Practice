# Chapter06-02
# 병행성(concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러일을 쉽게해결
# 병렬성(parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도 

# Generator Ex1

def generator_ex1():
    print('start')
    yield ' A point' # ex) 네이버에서 크롤링
    print('continue')
    yield ' B point' # ex) 구글에서 크롤링
    print('End')
    
temp = iter(generator_ex1())

# print(temp)
# print(next(temp))
# print(next(temp))
# print(next(temp))

for v in generator_ex1():
    pass
    # print(v)

print()
print()

# Generator Ex2
temp2 = [x * 3 for x in generator_ex1()] # for문으로 작성시 yield 옆에있는 코드가 맨마지막에 출력됌
temp3 = (x * 3 for x in generator_ex1()) # for문으로 작성시 yield 옆에있는 코드가 그자리에 맞게 출력됌

print(temp2)
print(temp3)

for i in temp2:
    print(i)

print()

for i in temp3:
    print(i)

print()
print()

# Generator Ex3 (중요함수)
# count, takewhile, filterfalse, accumulate, chain, product, groupby...

import itertools

gen1 = itertools.count(1, 2.5)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한

# 조건

gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

for v in gen2:
    pass
    # print(v)

print()

# 필터 반대
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5])

for v in gen3:
    print(v)

print()

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print(v)

print()
# 연결1
gen5 = itertools.chain('ABCDE', range(1,20,2))

print(list(gen5))

print()
# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))

print(list(gen6))

print()
# 개별
gen7 = itertools.product('ABCDE') # 튜플로 분리

print(list(gen7))

print()
# 연산(경우의 수)
gen8 = itertools.product('ABCDE', repeat=2) # 튜플로 분리

print(list(gen8))

print()
# 그룹화
gen9 = itertools.groupby('AAACBBCCCDDEEE')
'''
('AAABBCCCCDDEEE') 이렇게하면
A  :  ['A', 'A', 'A']
B  :  ['B', 'B']
C  :  ['C', 'C', 'C', 'C']
D  :  ['D', 'D']
E  :  ['E', 'E', 'E']

('AAACBBCCCDDEEE') 이렇게하면 순서대로
A  :  ['A', 'A', 'A']
C  :  ['C']
B  :  ['B', 'B']
C  :  ['C', 'C', 'C']
D  :  ['D', 'D']
E  :  ['E', 'E', 'E']
'''

# print(list(gen9))
for chr, group in gen9:
    print(chr, ' : ', list(group))