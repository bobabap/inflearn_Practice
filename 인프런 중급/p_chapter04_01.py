# Chapter04-01
# 시퀸스형
# 컨테이너(container : 서로다른 자료형[List, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형 [str, bytes, bytearray, array.array, mamoryview])
# 가변(List, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# a = [3, 3.0, 'a']
# print(a)

# 지능형 리스트(comprehending Lists)
chars = '+_)(*&^%$#@!)'
code_list1 = []


for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s)) # ord =x= chr 

print(code_list1)

print()
# comprehending Lists
code_list2 = [ord(s) for s in chars]

print(code_list2)

# comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars))) # 첫번째로 익명함수 함수 두번째는 리스트 자료구조형을 받음
# 재사용의 목적이 없다면, lambda 함수를 적용하는게 좋습니다.
'''
target = [1, 2, 3, 4, 5]

result = map(lambda x : x+1, target)

print(list(result))

>>>>>>>>>>>>>>>
리스트 안에 있는 값들을 str타입으로 변경
target = [ 1, 2, 3, 4, 5]
map(str, target)
'''
# --------------------------------------------
'''
target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(n):
    return True if n % 2 == 0 else False

result = filter(is_even, target)

print(list(result))

>>>>>>>>>>>>>>>
target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x : x%2==0, target)
print(list(result))
'''
# --------------------------------------------


# 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)

print()

print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()

# Generator 생성 매모리사용량 작아짐
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지x) iterator
# tuple_g = [ord(s) for s in chars] = [43, 95, 41, 40, 42, 38, 94, 37, 36, 35, 64, 33, 41]
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))


print(type(tuple_g))
print(next(tuple_g))
print(type(array_g))
print(array_g.tolist()) # array를 리스트로 반환해주는 함수는 tolist() 수치연산에 최적화

print()
print()

# 제네레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))
# 출력값 <generator object <genexpr> at 0x000001BFE0CB6C10>

for s in ('%s:' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

print()
print()

# 리스트 주의 ***
marks1 = [['~'] * 3 for _ in range(4)] # 다 다른 ID값
marks2 = [['~'] * 3] * 4


print(marks1)
print(marks2)

print()

# 수정
marks1[0][1] = 'X' # 이렇게 하는게 안전
marks2[0][1] = 'X'

print(marks1)
print(marks2)

# 증명 comprehending Lists ([])
print([id(i) for i in marks1]) # [1539967651648, 1539967651584, 1539967651392, 1539967651328]
print([id(i) for i in marks2]) # [1539967651136, 1539967651136, 1539967651136, 1539967651136]

