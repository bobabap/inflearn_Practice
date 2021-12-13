# print 기초1
print('Hello world')

print("-------------------------------------")
# print 기초2
print("Mary's comsmatics")
print(r"Mary's cosmetics")

print("-------------------------------------")
# print 기초3
print("신씨가 소리질렀다. \"도둑이야\".")

print("-------------------------------------")
# print 기초4
print("C:\windows")

print("-------------------------------------")
# print 기초5
print("안녕하세요. \n만나서\t\t반갑습니다")

print("-------------------------------------")
# print 기초6 여러 데이터 출력
print("오늘은", "일요일")

print("-------------------------------------")
# print 기초 7
print("naver", "kakao", "samsung", sep=";")
print("naver;kakao;samsung") # X

print("-------------------------------------")
# print 기초8
print("naver", "kakao", "sk", "samsung", sep="/")

print("-------------------------------------")
# print 기초9
print("first",end=" ");print("second")

print("-------------------------------------")
# print 기초10
print(5/3)

print("-------------------------------------")
# print 기초11 변수 사용하기
'''삼성전자라는 변수로 50,000원을 바인딩해보세요. 
삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.'''
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

# 띄어쓰기를 하고싶어서 변수로 바꿔서 계산
# S = "삼성 전자"
# S = 50000
# T = "총 평가금액"
# T = S * 10
# print(T)

print("-------------------------------------")
# print 기초12 변수 사용하기
'''시가총액 = 298조
   현재가   = 50,000원
   PER      = 15.79
   삼성전자의 표입니다 변수를 사용해서 바인딩 해보세요.'''
시가총액 = 298
현재가   = 50000
PER      = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

print("-------------------------------------")
# print 기초13 문자열 출력
'''s = "hello"
   t = "python"
   두 변수를 이용하여 아래와 같이 출력
   hello! python'''

s = "hello"
t = "python"
print(s + "!", t)

print("-------------------------------------")
# print 기초14 파이썬을 이용한 값 계산
'''2 + 2 * 3 = ?'''
print(2+2*3)

print("-------------------------------------")
# print 기초15 type 함수
'''type() 함수는 데이터 타입을 판별합니다.
   변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
   a = 128
   print(type(a)) = <class 'int'>
   '''
a = '132'
print(type(a))

print("-------------------------------------")
# print 기초16 문자열을 정수로 변환
'''문자열 '720'를 정수형으로 변환해보세요.

'''
num_str = "720"
print(int(num_str))
num_int = int(num_str)
print(num_int+1, type(num_int))

print("-------------------------------------")
# print 기초17 정수를 문자열 100으로 변환
'''정수 100을 문자열 '100'으로 변환해보세요.'''
num = 100
result = str(num)
print(result, type(result))


print("-------------------------------------")
# print 기초18
'''문자열 "15.79"를 실수(float) 타입으로 변환해보세요.'''
data = "15.79"
data = float(data)
print(data, type(data))


print("-------------------------------------")
# print 기초19
'''year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 
   이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.'''
# 답
year = "2020"
print(int(year)-3)  # 2017
print(int(year)-2)  # 2018
print(int(year)-1)  # 2019
# 내가 방식
year = "2020"
year = int(year)
print((year)-3, (year)-2, (year)-1)


print("-------------------------------------")
# print 기초20
'''에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다.
   총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)'''
월 = 48584
총금액 = 월 * 36
print(총금액)


print("-------------------------------------")
# print 기초21 문자열 인덱싱
'''letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.'''
# 내 답
letters = 'python'
print(letters[0],letters[2])
# 답
lang = 'python'
print(lang[0], lang[2])


print("-------------------------------------")
# print 기초22 문자열 슬라이싱
'''자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.'''
license_plate = "24가 2210"
# 실행 예: 2210
# 내 답
print(license_plate[3::])
# 답
license_plate = "24가 2210"
print(license_plate[-4:])


print("-------------------------------------")
# print 기초23 문자열 인덱싱
'''아래의 문자열에서 '홀' 만 출력하세요.'''
string = "홀짝홀짝홀짝"
print(string[::2])


print("-------------------------------------")
# print 기초24 문자열 슬라이싱
'''문자열을 거꾸로 뒤집어 출력하세요.'''
string = "PYTHON"
print(string[::-1])


print("-------------------------------------")
# print 기초25 문자열 치환
'''아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.'''
phone_number = "010-1111-2222"
# 실행 예 010 1111 2222
'''파이썬 문자열에서 replace 메서드를 사용하면 문자열을 일부를 치환할 수 있습니다.
   문자열은 수정할 수 없는 자료형이므로 기존 문자열은 그대로 두고 치환된 새로운 문자열이 리턴됩니다.'''
# 내 답
print(phone_number.replace('-', ' '))
# 정답
phone_number1 = phone_number.replace('-',' ')
print(phone_number1)


print("-------------------------------------")
# print 기초26 문자열 다루기
'''25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.'''
phone_number1 = phone_number.replace('-','')
print(phone_number1)


print("-------------------------------------")
# print 기초27 문자열 다루기
'''url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.'''
# 내 답
url = "http://sharebook.kr"
print(url[-2::])
# 정답 # url변수를 건드리지 않고 출력하는 연습
url_split = url.split('.')
print(url_split[-1])


print("-------------------------------------")
# print 기초28 문자열 immutable
'''아래 코드의 실행 결과를 예상해보세요.'''
# lang = 'python'
# lang[0] = 'P'
# print(lang)
# 내 답
'''Python 틀림'''
# 정답
'''
   문자열은 수정할 수 없습니다.
   실행 결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.
TypeError                                 Traceback (most recent call last)
<ipython-input-22-a0f3d05b669c> in <module>
      1 lang = "python"
----> 2 lang[0]= "P"
      3 print(lang)

TypeError: 'str' object does not support item assignment'''


print("-------------------------------------")
# print 기초29 replace 메서드
'''아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.'''
# 내 답
string = 'abcdfe2a354a32a'
string1 = string.replace('a','A')
print(string1)
# 답
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)


print("-------------------------------------")
# print 기초30 replace 메서드
'''아래 코드의 실행 결과를 예상해보세요.'''
string = 'abcd'
string.replace('b', 'B')
print(string)
# 내 예상 aBcd 와 개실수
# 정답 abcd
'''abcd가 그대로 출력됩니다. 왜냐하면 <-문자열은 변경할 수 없는 자료형->이기 때문입니다.
replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.'''