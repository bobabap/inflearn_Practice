# chapter05-01
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)

# 5! = 5*4*3*2*1
# 함수 객체

def factorial(n):
    '''Factorial Function -> n : int'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)

class A:
    pass

print(factorial(5))
print(factorial.__doc__)
print(type(factorial),type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial

print(var_func)
print(var_func(10))
print(list(map(var_func, range(1,11))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher- order function)
# map, filter, reduce
# es6

print(list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
print([var_func(i) for i in range(1, 6) if i % 2]) # 1~5 숫자중에서 홀수의 factorial을 구한다

print()
print()

# reduce
from functools import reduce
from operator import add

print(reduce(add, range(1,11))) # 하나하나씩 감소시켜가면서 누적시켜 더한다
print(sum(range(1,11))) # 이게 더빠름

# 익명함수(lambda)
# 가급적 주석 작성
# 가급적 함수 작성
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t: x + t, range(1,11))) # print(reduce(add, range(1,11)))

print()
print()

# callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인 / __call__ attribute가 있으면 호출가능
# 호출 가능 확인
print(callable(str), callable(list), callable(var_func), callable(factorial), callable(3.14))

# partial 사용법 : 인수 고정 -> 콜백 함수 사용
from operator import mul # from operator import mul, add 이렇게도 사용가능
from functools import partial

print(mul(10,10))

print()
# 인수 고정
five = partial(mul, 5) # 함수를 인자로 전달가능하고 함수를 변수에 할당 -> 일급함수의 특성

# 고정 추가
six = partial(five, 6)

print(five(10))
print(six())
print([five(i) for i in range(1,11)])
print(list(map(five, range(1,11)))) # map(적용시킬 함수, 적용할 값들)