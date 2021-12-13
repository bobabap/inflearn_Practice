from typing import KeysView


print("------------------------------------- 211")
# 211
'''함수의 호출 결과를 예측하라.'''
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")
'''
안녕
Hi
'''

print("------------------------------------- 212")
# 212
'''함수의 호출 결과를 예측하라.'''
def 함수(a, b):
    print(a + b)
함수(3, 4)
함수(7, 8)


print("------------------------------------- 213")
# 213
'''아래와 같은 에러가 발생하는 원인을 설명하라.'''
def 함수(문자열):
    print(문자열)
함수('문자열')
# 함수(문자열) -> TypeError
'''함수에 정의와 다르게 함수를 호출하고 있다. 
함수를 호출할 때 하나의 파라미터를 입력해야한다.'''


print("------------------------------------- 214")
# 214
'''아래와 같은 에러가 발생하는 원인을 설명하라.'''
def 함수(a, b):
    print(a + b)
# 함수("안녕", 3)
함수("안녕", '3')
'''정의된 함수는 같은 타입의 두 개의 값을 입력 받아 덧셈 연산을 적용하려는 의도로 설계됐습니다.
 하지만 함수를 호출 할때 문자열과 숫자를 입력해서 문자열과 숫자는 더할 수 없다는 에러가 발생합니다.'''


print("------------------------------------- 215")
# 215
'''하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는
print_with_smile 함수를 정의하라.'''
def print_with_smile(str):
    print(str + ':D')



print("------------------------------------- 216")
# 216
'''215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.'''
print_with_smile('아녕하세요')


print("------------------------------------- 217")
# 217
'''현재 가격을 입력받아 상한가(30%)를 출력하는 print_upper_price 함수를 정의하라.'''
def print_upper_price(price):
    print(price * 1.3)
print_upper_price(90)


print("------------------------------------- 218")
# 218
'''두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.'''
def print_sum(a, b):
    print(a + b)


print("------------------------------------- 219")
# 219
'''두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.'''
def print_arithmetic_operation(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)

print_arithmetic_operation(3, 4)


print("------------------------------------- 220")
# 220
'''새 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서
수를 비교하라.'''
# def print_max(a, b, c):
#     if a > b:
#         print(a)
#     elif c > a:
#         print(c)
#     else:
#         print(b)
# print_max(1000, 20000, 100)
# 정답
def print_max(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)
print_max(10 ,20, 5)


print("------------------------------------- 221")
# 221
def print_reverse(a) :
    print(a[::-1]) # reversed 로 하면 함수코드가나옴
print_reverse('cleanwater')


print("------------------------------------- 222")
# 222
'''성적 리스트를 입력 받아 평균을 출력하는 print_score함수를 정의하라.'''
def print_score(score_list):
    print(sum(score_list)/len(score_list))

print_score([1, 2, 3])


print("------------------------------------- 223")
# 223
'''하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.'''
def print_even(even):
    for i in even:
        if i % 2 == 0:
            print(i)

print_even([1, 3, 2, 10, 12, 11, 15])


print("------------------------------------- 224")
# 224
'''하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.'''
def print_keys(dic):
    for keys in dic.keys():
        print(keys)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})


print("------------------------------------- 225")
# 225
'''my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.'''
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
'''my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.'''
def print_value_by_key(my_dict, keys):
    print(my_dict[keys])
print_value_by_key(my_dict, "10/26")


print("------------------------------------- 226")
# 226
'''입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.'''
def print_5xn(string):
    chr_num = int(len(string) / 5) # print(int(1/5)) = 0
    for fivechr in range((chr_num + 1)):
        print(string[fivechr * 5: fivechr * 5 + 5]) # 15:20

print_5xn("아이엠어보이유알어걸")


print("------------------------------------- 227")
# 227
'''문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는
 print_mxn(string) 함수를 작성하라.'''
def print_mxn(string, count):
    chunk_num = int(len(string) / count)
    for x in range(chunk_num + 1):
        print(string[x * count: x * count + count])

print_mxn("아이엠어보이유알어걸", 3)


print("------------------------------------- 228")
# 228
'''연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary)함수를 정의하라.
회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.'''
# def calc_monthly_salary(annual_salary):
#     monthly = int(annual_salary / 12)
#     print(monthly)

# calc_monthly_salary(12000001)
'''입력된 값을 12로 나누고 형변환을 해서 1원 미만을 절사합니다.'''


print("------------------------------------- 229")
# 229
'''아래 코드의 실행 결과를 예측하라.'''
def my_print(a, b):
    print('left', a)
    print('right', b)

my_print(a=100, b=200)
'''
left 100
right 200
'''

print("------------------------------------- 230")
# 230
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)
'''
왼쪽: 200
오른쪽: 100
'''

print("------------------------------------- 231")
# 231
'''아래 코드르 실행한 결과를 예상하라.'''
def n_plus_1(n):
    result = n + 1
    
n_plus_1(3)
# print(result)
'''
4
4
아님 오류 함수 내부 호출불가 (함수 밖에서는 접근 불가)
'''

print("------------------------------------- 232")
# 232
'''문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.'''
# 내 답
# def make_url(n):
#     print('www.naver.com')
#     return

# 정답
def make_url(string):
    url = "www." + string + ".com"
    return url

# def make_url(string):
#     return "www." + string + ".com"
    
make_url('naver')
print(make_url('naver'))

print("------------------------------------- 233")
# 233
'''문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.'''
def make_list(string):
    return list(string)

make_list("abcd")
print(make_list("abcd"))

def make_list(string):
    my_list = []
    for 변수 in string:
        my_list.append(변수)
    return my_list

make_list("abcd")
print(make_list("abcd"))


print("------------------------------------- 234")
# 234
'''숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여
 리스트로 반환하는 pickup_even 함수를 구현하라'''
def pickup_even(int):
    pick_list = []
    for n in int:
        if n % 2 == 0:
            pick_list.append(n)
    return pick_list

pickup_even([3, 4, 5, 6, 7, 8])
print(pickup_even([3, 4, 5, 6, 7, 8]))


print("------------------------------------- 235")
# 235
'''콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.'''
def convert_int(string):
    return int(string.replace(',', ''))

convert_int("1,234,567")
print(convert_int("1,234,567"))


print("------------------------------------- 236")
# 236
'''아래 코드의 실행 결과를 예측하라.'''
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)
'''
22
'''


print("------------------------------------- 237")
# 237
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)
'''
22
'''


print("------------------------------------- 238")
# 238
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)
'''140'''


print("------------------------------------- 239")
# 239
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)
'''16'''
'''8번 함수2가 호출됩니다. 4번 라인으로 파이썬 인터프리터는 이동하고 이때
num에는 10이 바인딩됩니다. 5번 라인 코드를 실행하면 num이 12로 업데이트 됩니다.
6번라인의 코드를 실행하려고 하는데, 함수1이 호출됩니다. 1번 라인의 함수
정의부로 이동하며 num 값은 12로 바인딩됩니다. 2번 라인의 코드가 실행돼서 
16이 반환됩니다. 함수1의 동작을 끝마치고 함수 2의 6번 라인으로 돌아오고 
함수2도 return을 만나면서 16을 반환합니다.
8번 라인으로 돌아와 c 변수에는 16을 바인딩합니다.'''


print("------------------------------------- 240")
# 240
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
'''28'''