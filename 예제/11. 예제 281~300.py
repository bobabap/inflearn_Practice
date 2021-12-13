from os import write


print("------------------------------------- 281 클래스 정의")
# 281
'''다음 코드가 동작하도록 차 클래스를 정의하세요.'''
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

car = 차(2, 1000)
print(car.바퀴)
print(car.가격)



print("------------------------------------- 282 클래스 상속")
# 282
'''다음 코드가 동작하도록 차 클래스를 정의하세요.'''
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(차):
    pass



print("------------------------------------- 283 클래스 상속")
# 283
'''다음 코드가 동작하도록 차 클래스를 정의하세요.'''
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(차):
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

bicycle = 자전차(2, 100)
print(bicycle.가격)


print("------------------------------------- 284 클래스 상속")
# 284
'''다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.'''
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
        

class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격) # 자식 클래스에서 부모클래스의 내용을 사용하고 싶을경우 사용
        # 차.__init__(self, 바퀴, 가격)
        self.구동계 = 구동계


bicycle = 자전차(2, 100, '시마노')
print(bicycle.구동계)
print(bicycle.바퀴)



print("------------------------------------- 285 클래스 상속")
# 285
'''다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.'''
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
        

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격) # 자식 클래스에서 부모클래스의 내용을 사용하고 싶을경우 사용
        # 차.__init__(self, 바퀴, 가격)
        
    def 정보(self):
        print('바퀴수:', self.바퀴)
        print('가격:', self.가격)

car = 자동차(4, 1000)
car.정보()


print("------------------------------------- 286 부모 클래스 생성자 호출")
# 286
'''다음 코드가 동작하도록 자전차 클래스를 수정하세요.'''
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
    
    def 정보(self):
        print("바퀴수:", self.바퀴)
        print("가격:", self.가격)

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격) # 자식 클래스에서 부모클래스의 내용을 사용하고 싶을경우 사용
        # 차.__init__(self, 바퀴, 가격)
    
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계



bicycle = 자전차(2, 100, "시마노")
bicycle.정보()


print("------------------------------------- 287 부모 클래스 메서드 호출")
# 287
'''자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.'''
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
    
    def 정보(self):
        print("바퀴수:", self.바퀴)
        print("가격:", self.가격)

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격) # 자식 클래스에서 부모클래스의 내용을 사용하고 싶을경우 사용
        # 차.__init__(self, 바퀴, 가격)
    
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계
    
    def 정보(self):
        super().정보()
        print("구동계:", self.구동계)


bicycle = 자전차(2, 100, "시마노")
bicycle.정보()


print("------------------------------------- 288 메서드 오버라이딩")
# 288
'''다음 코드의 실행 결과를 예상해보세요.'''
class 부모:
  def 호출(self):
    print("부모호출")

class 자식(부모):
  def 호출(self):
    print("자식호출")

나 = 자식()
나.호출()


print("------------------------------------- 289 생성자")
# 289
'''다음 코드의 실행 결과를 예상해보세요.'''
class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
    def __init__(self):
        print("자식생성")
    
나 = 자식()


print("------------------------------------- 290 부모클래스 생성자 호출")
# 290
'''다음 코드의 실행 결과를 예상해보세요.'''
class 부모:
    def __init__(self):
        print("부모생성")
class 자식(부모):
    def __init__(self):
        print("자식생성")
        super(자식, self).__init__() #  super()로 기반 클래스 초기화하기 이렇게도 가능

나 = 자식()
'''
자식생성
부모생성
'''


print("------------------------------------- 291 파일 쓰기")
# 291
'''바탕화면에 '매수종목1.txt'파일을 생성한 후 다음과 같이 종목코드를 파일에 써보세요.'''
f = open("C:/Users/pc/Desktop/매수종목1.txt", mode="wt", encoding="utf-8")
f.write("005930\n")
f.write("005930\n")
f.write("005930")
f.close


print("------------------------------------- 292 파일 쓰기")
# 292
'''바탕화면에 '매수종목2.txt' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요.'''
f = open("C:/Users/pc/Desktop/매수종목2.txt", mode="wt", encoding="utf-8")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER\n")
f.close()



print("------------------------------------- 293 CSV 파일 쓰기")
# 293
import csv
'''바탕화면에 '매수종목.csv' 파일을 생성한 후 
다음과 같이 종목코드와 종목명을 파일에 써보세요. 인코딩은 'cp949'를 사용해야합니다.'''
f = open("C:/Users/pc/Desktop/매수종목.csv", mode="wt", encoding="cp949", newline='')
writer = csv.writer(f)
writer.writerow(['종목명', '종목코드', 'PER'])
writer.writerow(['삼성전자', '005930', '15.59'])
writer.writerow(['NAVER', '035420', '55.82'])
f.close


print("------------------------------------- 294 파일 읽기")
# 294
'''바탕화면에 생성한'매수종목1.txt'파일을 읽은 후 종목코드를 리슽트에 저장해보세요.'''
f = open("C:/Users/pc/Desktop/매수종목1.txt", encoding="utf-8")
lines = f.readlines()

codes = []
for line in lines:
    code = line.strip()
    codes.append(code)

print(codes)

f.close



print("------------------------------------- 295 파일 읽기")
# 295
f = open("C:/Users/pc/Desktop/매수종목2.txt", encoding="utf-8")
lines = f.readlines()

data = {}
for line in lines:
    line = line.strip()     # '\n' 제거
    k, v = line.split()
    #print(k, v)
    data[k] = v

print(data)
f.close()


print("------------------------------------- 296 예외처리")
# 296
'''문자열 PER (Price to Earning Ratio) 값을 실수로 변환할 때 에러가 발생합니다. 예외처리를
통해 에러가 발생하는 PER은 0으로 출력하세요.
per = ["10.31", "", "8.00"]

for i in per:
    print(float(i))
'''
per = ["10.31", "", "8.00"]
new_per = []
for i in per:
    try:
        print(float(i))
    except:
        print(0)
    new_per.append(i)
print()
print(new_per)

print("------------------------------------- 297 예외처리 및 리스트에 저장")
# 297
'''문자열로 표현된 PER값을 실수로 변환한 후 이를 새로운 리스트에 저장해보세요.
per = ["10.31", "", "8.00"]

for i in per:
    print(float(per))
'''
per = ["10.31", "", "8.00"]
new_per = []

for i in per:
    try:
        v = float(i)
    except:
        v = 0
    new_per.append(v)
print(new_per)


print("------------------------------------- 298 특정 예외만 처리하기")
# 298
'''어떤 값을 0으로 나누면 ZeroDivisionError 에러가 발생합니다.
 try ~ except로 모든 에러에 대해 예외처리하지 말고 ZeroDivisionError 에러만 예외처리해보세요.'''
try:
    b = 3 / 0
except ZeroDivisionError:
    print("0으로 나눌수 없습니다.")



print("------------------------------------- 299 예외의 메시지 출력하기")
# 299
'''다음과 같은 코드 구조를 사용하면 예외 발생 시 에러 메시지를 변수로 바인딩할 수 있습니다.'''
'''
try:
    실행코드
except 예외 as 변수:
    예외처리코드 
'''
'''리스트의 인덱싱에 대해 에러를 출력해보세요.'''
data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as ek:
        print(ek)




print("------------------------------------- 300 try, except, else, finally 구조 사용해보기")
# 300
'''파이썬 예외처리는 다음과 같은 구조를 가질 수 있습니다.'''
'''
try:
    실행 코드
except:
    예외가 발생했을 때 수행할 코드
else:
    예외가 발생하지 않았을 때 수행할 코드
finally:
    예외 발생 여부와 상관없이 항상 수행할 코드
'''
'''아래의 코드에 대해서 예외처리를 사용하고 try, except, else, finally에
   적당한 코드를 작성해봅시다.
   else와 finally는 적당한 문구를 print하시면 됩니다.'''
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print('0')
    else:
        print('clean data')
    finally:
        print('')