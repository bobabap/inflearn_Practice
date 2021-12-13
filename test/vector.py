'''
벡터 합과 차
원소별로 계산 : 다음을 구현하고 싶음
[1, 2] 더하기 [3, 4] = [4, 6]
[5, 3] 빼기 [1, 7] = [4, -4]
'''
def vector_add(v, w):
    """adds two vectors componentwise"""
    return [v_i + w_i for v_i, w_i in zip(v,w)]

print(vector_add([1,2], [3,4]))


print(vector_add([1,2,3], [3,4,5]))


v = [1, 2, 3]
w = [2, 3, 4]
z = vector_add(v, w)
y = vector_add(z, v)
print(y)


print()
print()

def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]


print(vector_subtract([0, 0, 1], [1, 2, 3]))


print()
print()

'''
여러 개의 벡터들의 합
벡터들의 리스트가 있을 때, 리스트 내의 벡터들을 원소 별로 합하기
'''
def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result


vectors = [[1, 2, 3],
           [2, 3, 0],
           [0, 1, -2]]

print(vector_sum(vectors))

# 내부적으로는 다음과 동치
# vector_add(vector_add([1, 2, 3], [2, 3, 0]), [0, 1, -2])

print()
print()

'''
스칼라 곱
목표 : 3*[1, 2, 3] = [3, 6, 9]
'''

def scalar_multiply(c, v):
    return [c * vi for vi in v]

print('''3*[1, 2, 3] = [3, 6, 9] : ''', scalar_multiply(3, [1, 2, 3]))

print()
print()

'''
dot product
목표 :
dot( [1, 2, 3], [0, 1, 2]) = sum([1 * 0, 2 * 1, 3 * 2]) = sum([0, 2, 6]) = 8
'''
def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

print("""v_1 * w_1 + ... + v_n * w_n : """, dot([1, 2, 3], [0, 1, 2]))


print()
print()

'''
제곱합
벡터 원소들의 제곱의 합
'''
def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n : """
    return dot(v, v)

print("""v_1 * v_1 + ... + v_n * v_n : """, sum_of_squares([0, 1, 2]))

print()
'''벡터의 크기(magnitude) : 제곱합의 제곱근'''
import math
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

print(magnitude([3, 4]))
print(magnitude([5, 12]))

print()
print()
'''
벡터 사이의 거리
한 벡터에서 다른 벡터를 뺀 후, 크기를 구하는 것과 동일
'''
def distance(v, w):
    return magnitude(vector_subtract(v, w))

print(distance([1, 2], [2, 3]))