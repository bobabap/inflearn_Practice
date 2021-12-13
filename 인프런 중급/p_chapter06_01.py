# Chapter06-01
# 병행성(concurrency)
# Iterator, Generator

# 파이썬 반복 가능한 타입
# collectionsm, text, list, Dict, set, tuple, unoacking, *args...: iterable

# 반복 가능한 이유? -> iter(x) 함수 호출
t = "ABCDEFGHIJKLMNOPQRSTUWXYZ"

print(dir(t))

for c in t:
    pass
    # print(c)

print('-------------------------------------------------------')
# 위와같음
# while
w = iter(t) # '__next__',

while True:
    try:
        print(next(w))
    except StopIteration:
        break
'''
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
'''

print()

# 반복형 확인

from collections import abc

# print(dir(t))
print(hasattr(t, '__iter__')) # __iter__가 있는가?
print(isinstance(t, abc.Iterable)) # iterable 클래스를 상속 받았는지 확인 isinstance(확인하고자 하는 데이터 값, 확인하고자 하는 데이터 타입)

print()
print()


# next 패턴
class WordSplitter:
    
    def __init__(self, text):
        print('--------------------__init__')
        self._idx = 0
        self._text = text.split(' ')
    
    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx] + '-------------------------------next함수에 try문'
        except IndexError:
            raise StopIteration('stopped Iteration ^.^')
        self._idx += 1
        return word
    
    def __repr__(self): # 이 함수가 없다면 print(wi) 는 <__main__.WordSplitter object at 0x000002C05C75AEB0> 이렇게 호출됌
        print('--------------------__repr__')
        return 'WordSplitter(%s)' % (self._text)

wi = WordSplitter('Do today what you could do tommorrow')


print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

print()

print(wi)

print()
print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(corotine) 구현과 연동 -> 병행성 병렬성을 알수있음
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터 내부적으로 다음에 반환될 위치정보 기억
        return

    def __repr__(self):
        return 'WordSplitGenerator(%s)' % (self._text)

wg = WordSplitGenerator('Do today what you could do tommorrow')

wt = iter(wg)

print(wt, ' , ', wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))

print()
print()