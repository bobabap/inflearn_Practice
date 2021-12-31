# Chapter04-02
# 시퀸스형
# 컨테이너(container : 서로다른 자료형[List, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형 [str, bytes, bytearray, array.array, mamoryview])
# 가변(List, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b

print(divmod(100, 9)) # 몫과 나머지
print(divmod(*(100, 9)))
print(*(divmod(100,9)))

print()

x, y, *rest = range(10)
print(x, y, rest)

x, y, *rest = range(2)
print(x, y, rest)

x, y, i, z, *rest = 1, 2, 3, 4, 5
print(x, y, i, z, rest)

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (15, 20, 25) # 계속바뀜 Tuple
m = [15, 20, 25] # (불변)
print(l, id(l))
print(m, id(m))

l = l * 2 # 재할당
m = m * 2
print(l, id(l))
print(m, id(m))


l *= 2 # 수정이 불가능하기 때문에 ID값이 매번 다름
m *= 2
print(l, id(l))
print(m, id(m))

print()
print()

# sort vs sorted
# reverse, key=len, key=str.lower, key=func...

#sorted : 정렬 후 새로운 객체 반환 (원본그대로)
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key=len))
print('sorted - ', sorted(f_list, key=lambda x : x[-1])) # 끝글자 기준 a b c 순서
print('sorted - ', sorted(f_list, key=lambda x:x[-1], reverse=True))

print()

print('sorted - ',f_list)

print()

#sort : 정렬 후 객체 직접 변경 (원본 변경)

# 반환 값 확인(None)
print('sort - ', f_list.sort(), f_list)
print('sort - ', f_list.sort(reverse=True), f_list)
print('sort - ', f_list.sort(key=len), f_list)
print('sort - ', f_list.sort(key=lambda x : x[-1]), f_list)
print('sort - ', f_list.sort(key=lambda x : x[-1], reverse=True), f_list)

# List vs Array 적합 한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용 List
# 숫자 기반 : 배열(리스트와 거의 호환) Array