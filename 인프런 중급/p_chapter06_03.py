# Chapter06-03
# 병행성(concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러일을 쉽게해결
# 병렬성(parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도 
# 코루틴(coroutine)

# 코루틴 : 단일 (싱글) 스레드, 스텍을 기반으로 동작하는 비동기 작업
# 쓰레드 : os 관리, cpu 코어에서 실시간, 시분할 비동기 작업 -> 멀티쓰레드
# yield, send : 메인 <-> 서브 양방향 통신
# 코루틴 제어, 상태, 양반향 전송

# 서브루틴 : 메인루틴 호출 - > 서브루틴에서 수행(흐름제어)

# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍
# 코루틴 : 쓰레드에 비해 오버헤드 감소

# 스레드 : 싱글쓰레드 -> 멀티쓰레드 -> 복잡 -> 공유되는 자원
#  -> 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성증가 

# def -> async, yield -> await



# 코루틴 Ex1

def coroutine1():
    print('>>> coroutione started.')
    i = yield
    print('>>> coroutine receiced : {}'.format(i))


# 메인 루틴
# 제네레이터 선언
cr1 = coroutine1()

print(cr1, type(cr1))

# yield 지정까지 서브루틴 수행
# next(cr1)
# next(cr1) # >>> coroutine receiced : None

# 기본 전달 값 None
# 값 전송
# cr1.send(100)

# 잘못된 사용
# cr2 = coroutine1()
# cr2.send(100)  next없이 바로사용 한경우 TypeError: can't send non-None value to a just-started generator

print()

# 코루틴 Ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : Yield 대기 상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x)) # x를 메인루틴에서 받아서 출력
    y = yield x # y를 메인루틴에서 받아서 출력하고 이때 x를 서브루틴에서 메인루틴으로 전달
    # 왼쪽에있으면 받는거 오른쪽에있으면 주는거 y = yield x 양방향으로 주고받음
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))


cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))

print(next(cr3))

cr3.send(100)
# print(cr3.send(100)) = 110

print()
print()

# 코루틴 Ex3
# stopIteration 자동 처리(3.5 -> await)
# 중첩 코루틴 처리

def generator1():
    for x in "AB":
        yield x
    for y in range(1,4):
        yield y

t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1))

t2 = generator1()

print(list(t2))

print()
print()

def generator2():
    yield from "AB" # 이터레이블한 데이터를 순차적으로 끝날때까지 반환하겠다
    yield from range(1,4)

t3 = generator2()

print(next(t3))
print(next(t3))
print(next(t3))