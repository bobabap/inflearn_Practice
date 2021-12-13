# vartest.py
a = 1
def vartest(a):
    a = a +2
vartest(a)
print(a)

'''함수 안에서 함수 밖의 변수를 변경하는 방법 global은 안쓰는게 좋음 함수는 독립적이어야함
외부 변수에 족속적인 함수는 그다지 좋은 함수가 아니다.'''
a = 1
def vartest(a):
    a = a +1
    return a

a = vartest(a)
print(a)