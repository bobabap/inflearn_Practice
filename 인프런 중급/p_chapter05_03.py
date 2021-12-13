# chapter05-03
# 일급 함수 (일급 객체)
# 클로저 기초
# 외부에서 호출괸 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능

# closure 사용
def closure_ex1():
    # Free variable
    # 클로저 영역
    series = [] # 자유 변수
    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager

avg_closure1 = closure_ex1()
 
print(avg_closure1(10))
print(avg_closure1(20))
print(avg_closure1(30))

print()
print()

# funcion inspection 함수 내부
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars) # 자유 변수 ('series',)
print(avg_closure1.__closure__[0].cell_contents) # [10, 20, 30]


print()
print()


# 잘못된 클로저 사용
# def closure_ex2():
#     # Free variable
#     cnt = 0
#     total = 0

#     def averager(v):
#         cnt += 1
#         total += v
#         return total / cnt
#     return averager

# avg_closure2 = closure_ex2()

# print(avg_closure2(10))

def closure_ex3():
    # Free variable
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))




'''
아래와 같이 글로벌 함수로 전역변수의 값을 지역내에서 수정하는것은 권장하지않음
'''
cnt = 0
total = 0
def closure_ex3():
    # Free variable
    
    def averager(v):
        global cnt
        global total
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))