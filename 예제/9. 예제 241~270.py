print("------------------------------------- 241")
# 241
'''datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.'''
import datetime
now = datetime.datetime.now()
print(now)


print("------------------------------------- 242")
# 242
now = datetime.datetime.now()
print(now, type(now))


print("------------------------------------- 243 timedelta")
# 243
'''datetime 모듈의 timedalta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 
전의 날짜를 화면에 출력해보세요.'''
import datetime
now = datetime.datetime.now()

for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)
print(delta)


print("------------------------------------- 244 strftime")
# 244
'''현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. 
    strftime 메서드를 사용하세요.'''
import datetime
now = datetime.datetime.now()
print(now.strftime('%H:%M:%S'))


print("------------------------------------- 245")
# 245
import datetime

day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))


print("------------------------------------- 246 sleep 함수")
# 246
'''time 모듈, datetime 모듈을 사용해서
 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.'''
import time
import datetime

# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)


print("------------------------------------- 247 모듈 임포트")
# 247
'''모듈을 임포트하는 4가지 방식에 대해 설명해보세요.'''
'''
첫 번째, import A.
두 번째, from B import A.
세 번째 from A import * (좋지않음)
'''




print("------------------------------------- 248 os 모듈")
# 248
'''os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.'''
import os
print(os.getcwd())


print("------------------------------------- 249 rename 함수")
# 249
'''바탕화면 텍스트 파일을 하나 생성한 후 os 모듈의 rename함수를 호출하여 해당 파일 이름을
변경해 보세요'''
# import os # \가아닌 /으로 해야한다.
# os.rename('C:/Users/pc/Desktop/이름을 바꾸시오..txt', 'C:/Users/pc/Desktop/곤잘레스.txt')


print("------------------------------------- 250 numpy")
# 250
'''numpy모듈의 arange 함수를 사용해서 0.0부터 5.0까지 0.1 씩 증가하는 값을 화면에
출력해보세요'''
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(round(i, 1))


print("------------------------------------- 251 클래스, 객체, 인스턴스")
# 251
'''클래스, 객체, 인스턴스에 대해 설명해봅시다.'''
# 클래스
'''A class is a code template for creating objects. Objects
 have member variables and have behaviour associated with them.
 In python a class is created by the keyword class .
  An object is created using the constructor of the class.
 This object will then be called the instance of the class.'''
# 인스턴스
''' An individual object of a certain class.
An object obj that belongs to a class Circle, for example, is an instance of the class Circle.
 Instantiation − The creation of an instance of a class. 
Method − A special kind of function that is defined in a class definition.'''
# 객체
''' An object is the collection of various data and functions that operate on those data.'''


print("------------------------------------- 252 클래스 정의")
# 252
'''비어있는 사람 (Human) 클래스를 "정의" 해보세요.'''
class Human:
    pass


print("------------------------------------- 253 인스턴스 생성")
# 253
'''사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.'''
areum = Human


print("------------------------------------- 254 클래스 생성자-1")
# 254
'''사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.'''
class Human:
    def __init__(self):
        print("응애응애")
areum = Human()



print("------------------------------------- 255 클래스 생성자-2")
# 255
'''사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.'''
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human("조아름", 25, "여자")
print(areum.name)



print("------------------------------------- 256 인스턴스 속성에 접근")
# 256
'''255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여
값을 출력'''
'''이름: 조아름, 나이: 25, 성별: 여자'''
'''인스턴스 변수에 접근하여 값을 가져오는 예
areum.age
25
'''
print(areum.age)
    


print("------------------------------------- 257 클래스 메소드 - 1")
# 257
'''사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.'''
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.sex))
areum = Human("아름", 25, "여자")
areum.who()


print("------------------------------------- 258 클래스 메소드 - 2")
# 258
'''사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.'''
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def who(self):
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.sex))    
    
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human("불명", "미상", "모름")
areum.who()

areum.setInfo("아름", 25, "여자")
areum.who()
print(dir(areum)) # dir에 'age', 'name', 'setInfo', 'sex', 'who' 가 추가됌


print("------------------------------------- 259 클래스 소멸자")
# 259
'''사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.'''
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __del__(self):
        print("나의 죽음을 알리지마라.")

    def who(self):
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.sex))    
        
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
areum = Human("아름", 25, "여자")
del(areum)

print("------------------------------------- 260 에러의 원인")
# 260
'''아래와 같은 에러가 발생한 원인에 대해 설명하세요.'''
class OMG : 
    def print(self, say):
        print("Oh my god")
# mystock = OMG()
# mystock.print()
'''TypeError: print() takes 0 positional arguments but 1 was given'''




print("------------------------------------- 261 Stock 클래스 생성")
# 261
'''주식 종목에 대한 정보를 저장하는 Stock 클래스를 정의해보세요.
클래스는 속성과 메서드를 갖고 있지 않습니다.'''
class stock:
    pass





print("------------------------------------- 262 생성자")
# 262
'''stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록
 생성자를 정의해보세요.'''
class stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
삼성 = stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)



print("------------------------------------- 263 메서드")
# 263
'''객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.'''
class stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def set_name(self, name):
        self.name = name
        
a = stock(None, None)
a.set_name('삼성전자')
print(a.name)



print("------------------------------------- 264 메서드")
# 264
'''객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가해보세요.'''
class stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
a = stock(None, None)
a.set_code("005930")
print(a.code)


print("------------------------------------- 265 메서드")
# 265
'''종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여
종목명과 종목코드를 얻고 이를 출력해보세요.'''
class stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name
        
    def get_code(self):
        return self.code
        
삼성 = stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)
print(삼성.get_name())
print(삼성.get_code())




print("------------------------------------- 266 객체의 속성값 업데이트")
# 266
'''생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요.
PER, PBR, 배당수익률은 float 타입입니다.'''
class stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name
        
    def get_code(self):
        return self.code





print("------------------------------------- 267")
# 267
삼성 = stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(삼성.배당수익률)




print("------------------------------------- 268 객체의 속성 수정")
# 268
'''PER, PBR, 배당수익률은 변경될 수 있는 값입니다. 이 값을 변경할 때 사용하는 set_per,
set_pbr, set_dividend 메서드를 추가하세요.'''
class stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name
        
    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend





print("------------------------------------- 269 객체의 속성 수정")
# 269
'''267번에서 생성한 객체에 set_per 메서드를 호출하여 per 값을 12.75로 수정해보세요.'''
삼성 = stock("삼성전자", "005930", 15.79, 1.33, 2.83)
삼성.set_per(12.75)
print(삼성.per)


print("------------------------------------- 270 여러 종목의 객체 생성")
# 270
'''아래의 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장하세요.
파이썬 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력해보세요.'''
class stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name
        
    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend
종목 = []
삼성전자 = stock('삼성전자', '005930', 15.79, 1.33, 2.83)
현대차 = stock('현대차', '005480', 8.70, 0.35, 4.27)
LG전자 = stock('LG전자', '066570', 317.14, 0.69, 1.37)

종목.append(삼성전자)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print('code:', i.code, "   ", 'PER:', i.per) # i-> Stock 클래스의 객체를 바인딩하기 때문

