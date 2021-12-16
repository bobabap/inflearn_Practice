print("---------------------------------------")
# Q1 문자열 바꾸기
Q1 = 'a:b:c:d'
q = Q1.split(":")
print(q)
p = ("#").join(q)
print(p)

print("---------------------------------------")
# Q2 딕셔너리 값 추출하기
a = {'A':90, 'B':80}
try:
    a['C']
except:
    a = {'A':90, 'B':80, 'C' : 70}
print(a['C'])
# 정답 
a = {'A':90, 'B':80}
a.get('C', 70)

print("---------------------------------------")
# Q3 리스트의 더하기와 extend 함수
a = [1, 2, 3]
print(id(a), a)
a = a + [4,5]
print(id(a), a)
# 차이점
b = [1, 2, 3]
print(id(b), b)
b.extend([4, 5])
print(b)
print(id(b), b)


print("---------------------------------------")
# Q4 리스트 총합 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result = []
for i in A:
    if i > 50:
        result.append(i)
print(sum(result))
# 정답
result = 0
while A:
    mark = A.pop()
    if mark >= 50:
        result += mark
print(result)


print("---------------------------------------")
# Q5 피보나치 함수
'''0, 1, 1, 2, 3, 5, 8, 13, ...'''
def fibonachi(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonachi(n-2) + fibonachi(n - 1)

for i in range(10):
    print(fibonachi(i))

print("---------------------------------------")
# Q6 숫자의 총합 구하기
# user_input = input("숫자들을 입력하시오: ")
# numbers = user_input.split(",")
# number_sum = 0
# for number in numbers:
#     number_sum += int(number)
# print(number_sum)


print("---------------------------------------")
# Q7 한 줄 구구단
# user_input = input("구구단을 출력할 숫자를 입력하세요(2~9): ")
# numbers = user_input
# for i in range(1, int(numbers)):
#     for x in range(1, 10):
#         print(x * int(numbers),end=' ')
# 정답
# user_input = input("구구단을 출력할 숫자를 입력하세요(2~9): ")
# dan = int(user_input)
# for i in range(1, 10):
#     print(i*dan, end=' ')


print("---------------------------------------")
# Q8 역순 저장
# f = open("C:/p_study/abc.txt", 'r')
# lines = f.readlines()
# print(lines) # ['AAA\n', 'BBB\n', 'CCC\n', 'DDD\n', 'EEE\n']
# f.close()
# # 수정
# lines.reverse()

# f = open("C:/p_study/abc.txt", 'w')
# for line in lines:
#     line = line.strip()
#     f.write(line)
#     f.write('\n')
# f.close()

a = ('EEE\n').strip()
print(a)

a = ('EEE\n')
print(a)


print("---------------------------------------")
# Q9 평균값 구하기
# f = open("C:/p_study/sample.txt", 'r')
# lines = f.readlines()
# f.close()
# # 결과 저장
# total = 0
# for line in lines:
#     score = int(line)
#     total += score
# average = total / len(lines)

# f = open("C:/p_study/result.txt", 'w')
# f.write("average: ")
# f.write(str(average))
# f.write("\n")
# f.write("total: ")
# f.write(str(total))

# f.close()

print("---------------------------------------")
# Q10 사칙연산 계산기
class Calculator():
    def __init__(self, numberlist):
        self.numberlist = numberlist

    def sum(self):
        result = 0
        for num in self.numberlist:
            result += num
        return result

    def avg(self):
        total = self.sum()
        return total / len(self.numberlist)

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())


print("---------------------------------------")
# Q11 묘듈 사용법
'''
import sys
sys.path.append("c:/doit")
import mymod
'''
# C:\Users\home>set PYTHONPATH=c:\doit
# C:\Users\home>python
# import mymod

# C:\Users\home>cd c:\doit
# C:\doit>python
# import mymod



print("---------------------------------------")
# Q12 오류와 예외 처리
result = 0

try:
    [1, 2, 3][3] # 여기서 에러 발생시 밑에 구분 실행안됌
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)


print("---------------------------------------")
# Q13 DashiInsert 함수
data = "4546793"
numbers = list(map(int, data))
result = []
# print(numbers)

for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1:
        is_odd = num % 2 == 1
        is_next_odd = numbers[i+1] % 2 == 1
        if is_odd and is_next_odd:
            result.append("-")
        elif not is_odd and not is_next_odd:
            result.append("*")

print("".join(result))


print("---------------------------------------")
# Q14 문자열 압축하기
def compress_string(s):
    _c = "" # a,b,c,a
    cnt = 0 # 3,2,6,1
    result = "" # a(1+1+1) b(1+1) c(1+1+1+1+1+1) a(1)
    for c in s:
        if c!=_c:
            _c = c
            if cnt:
                result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt += 1
    if cnt:
        result += str(cnt)
    return result

print(compress_string("aaabbcccccca"))



print("---------------------------------------")
# Q15 Duplicate Numbers
def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10

print(chkDupNum("0123456789"))      # True 리턴
print(chkDupNum("01234"))           # False 리턴
print(chkDupNum("01234567890"))     # False 리턴
print(chkDupNum("6789012345"))      # True 리턴
print(chkDupNum("012322456789"))    # False 리턴


print("---------------------------------------")
# Q16 모스 부호 해독
mos_dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(mos_dic[char])
        result.append(" ")
    return "".join(result)

print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))


print("---------------------------------------")
# Q17 기초 메타 문자
import re

p = re.compile("a[.]{3,}b")

print(p.match("acccb"))    # None
print(p.match("a....b"))   # 매치 객체 출력 .이 3개 이하이면 None출력
print(p.match("aaab"))     # None
print(p.match("a.cccb"))   # None


print("---------------------------------------")
# Q18 문자열 검색
import re
p = re.compile("[a-z]+")
m = p.search("5 python")
print(m.start() + m.end())
a = "5 python"
print(a[2:7])


print("---------------------------------------")
# Q19 그루핑
pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
import re

data = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####", data)

print(result)


print("---------------------------------------")
# Q19 그루핑
pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("pahkey@gmail.com"))
print(pat.match("pahkey@gmail.com.com"))
print(pat.match("kim@daum.net"))
print(pat.match("lee@myhome.co.kr"))