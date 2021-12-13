# chapter02-03
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Auther : Yang
    Date : 2021.09.26
    Description : Class, Static, Instance Method

    """
    # 클래스 변수(모든 인스턴스가 공유) 선언하는곳
    price_per_raise = 1.0
    
    def __init__(self, company, details):
        self._company = company # instans 변수
        self._details = details
    def __str__(self): # 사용자 입장에서 출력, print문으로 정보를 확인할때 __str__,  __repr__ 둘이 같이 실행하면 __str__만 실행됌
        return 'str : {} - {}'.format(self._company, self._details) # 인스턴스 메소드
    
    def __repr__(self): # 객체 그대로 표현해주고싶을때 개발자 입장에서 엄격한 타입을 인식할수있는
        return 'repr : {} - {}'.format(self._company, self._details)
    # Instance Method
    # self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before car price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After car price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased')

    # Staric Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. this car is not Bmw.'








# self 의미
car1 = Car('Ferrari', {'color': 'white','horsepower' : 400,'price' : 8000})
car2 = Car('Bmw', {'color' : 'black','horsepower' : 270,'price' : 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격 정보(직접 접근) 좋지않음
print(car1._details.get('price'))
print(car2._details['price'])

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 메소드 미사용) 나이스하지않음
Car.price_per_raise = 1.4

# 가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

print()
# >>>>>>>>>>>>>>>>>>>>>

# 가격 인상(클래스 메소드 사용) 인스턴스를 만들지 않아도 class의 메서드를 바로 실행할 수 있다
Car.raise_price(1.6)

# 가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 인스턴스로 호출(staticmethod)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 클래스로 호출(staticmethod)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))

# Sorry. this car is not Bmw. 
# OK! This car is Bmw
