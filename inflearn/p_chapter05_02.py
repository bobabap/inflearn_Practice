# chapter05-02
# 일급 함수 (일급 객체)
# 클로저 기초

# 파이썬 변수 범위(scope)

# Ex1

def func_v1(a):
    print(a)
    print(b)

# func_v1(10)

# Ex2
b = 20

def func_v2(a):
    print(a)
    print(b)

func_v2(10)
'''
10
20 
'''

print()
# Ex3 

c = 30

def func_v3(a):
    global c
    c = 40 # 안쪽에 같은 c가있다면 먼저 로컬변수로 인식함 로컬이 먼저임
    print(a)
    print(c)
    
print('>>',c) # 30
func_v3(10) # 10, 40
print('>>>',c) # 40

'''
>> 30
10
40
>>> 40
'''


print()
print()

c = 30

def func_v3(a):
    global c
    print(a)
    print(c)
    c = 40 # global 변수를 40 으로 치환

print('>>',c) # 30
func_v3(10) # 10, 30
print('>>>',c) # 40

'''
>> 30
10
30
>>> 40
'''


print()
print()


c = 30

def func_v3(a):
    c = 40
    print(a)
    print(c)
    

print('>>',c) # 30
func_v3(10) # 10, 40
print('>>>',c) # 30

'''
>> 30
10
40
>>> 30
'''

print()
print()


c = 30

def func_v3(a):
    global c
    print(a)
    print(c)
    

print('>>',c) # 30
func_v3(10) # 10, 30
print('>>>',c) # 30

'''
>> 30
10
30
>>> 30
'''


print()
print()


# Closure(클로저) 사용 이유
# 서버 프로그래밍 -> 동시성(concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 -> Erlang
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(coroutine) (병행성처리) 프로그래밍에 강점

a = 100

print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1,51))) # range 50 -> 49
print(sum(range(51,101)))

# 클래스 이용
class Averager():
    def __init__(self): # Closure(클로저) 사용
        self._series = [] # 상태를 기억하고 누적

    def __call__(self, v): # 클래스를 함수처럼 사용가능
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
averager_cls = Averager()

print(dir(averager_cls))

print()
# 누적
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))
print(averager_cls(70))
