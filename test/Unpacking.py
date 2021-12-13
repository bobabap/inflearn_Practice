def cal(first, op, second):
     if op == '+':
         return first + second
     if op == '/':
         return first / second
     if op == '-':
         return first - second
     if op == '*':
         return first * second


prob = {'first': 12, 'second': 34, 'op': '*'}

cal(**prob) # 결과 : 408
print(cal(**prob))

'''
위치인자의 unpacking처럼 unpacking되는 인자는 매개변수의 키워드 매개변수와 일치해야합니다.

만약 비어있는 인자를 unpacking를 하면 무시합니다. 이러한 특성이 있기 때문에 함수의 packing과 unpacking을 이용하여, 
다음과 같이 어떠한 함수에도 반응하는 함수를 작성할 수 있습니다.

함수와 함수에 인자들을 받아서 시작전 알림과 함께 함수를 실행시켜주는 함수입니다.
'''

def start(func, *args, **kwargs):
    print("함수를 시작합니다.")
    return func(*args, **kwargs)

start(print, '안녕하세요', '파이썬 꿀잼!', sep='~~ ')

def sum_a_b(a, b):
     return a + b

result = start(sum_a_b, 1, 2) # 함수를 시작합니다.
print(result) # 3
