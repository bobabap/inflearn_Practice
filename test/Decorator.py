import time

def perf_clock(func):
     def perf_clocked(*args): # 팩킹을 안했을 때 -> __main__.time_func() argument after * must be an iterable, not float
          # 함수 시작 시간
          st = time.perf_counter()
          # 함수 실행
          result = func(*args)
          # 함수 종료 시간
          et = time.perf_counter() - st
          # 실행 함수면
          name = func.__name__
          # 함수 매개변수
          arg_str = ', '.join(repr(arg) for arg in args)
          # 결과 출력
          print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))


          return result
     return perf_clocked


@perf_clock
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)



print('-' * 40, 'Called Decorator -> time_func')
print()
time_func(1.5)
print('-' * 40, 'Called Decorator -> time_func')
print()
sum_func(100, 200, 300, 400, 500)


'''
<return result 없는거>
---------------------------------------- Called Decorator -> time_func

[1.50629s] time_func(1.5) -> None
---------------------------------------- Called Decorator -> time_func

[0.00000s] sum_func(100, 200, 300, 400, 500) -> 1500

'''


'''
<return result 있는거>
---------------------------------------- Called Decorator -> time_func

[1.50144s] time_func(1.5) -> None
---------------------------------------- Called Decorator -> time_func

[0.00000s] sum_func(100, 200, 300, 400, 500) -> 1500
'''