# chapter02-02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Auther : Yang
    Date : 2021.09.25
    사용법 : 뢀뢀
    """
    # 클래스 변수(모든 인스턴스가 공유) 선언하는곳
    
    car_count = 0
    
    
    def __init__(self, company, details):
        self._company = company # instans 변수
        self._details = details
        Car.car_count += 1
    def __str__(self): # 사용자 입장에서 출력, print문으로 정보를 확인할때 __str__,  __repr__ 둘이 같이 실행하면 __str__만 실행됌
        return 'str : {} - {}'.format(self._company, self._details) # 인스턴스 메소드
    
    def __repr__(self): # 객체 그대로 표현해주고싶을때 개발자 입장에서 엄격한 타입을 인식할수있는
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
    
    def __del__(self):
        Car.car_count -= 1

car1 = Car('Ferrari', {'color': 'white','horsepower' : 400,'price' : 8000})
car2 = Car('Bmw', {'color' : 'black','horsepower' : 270,'price' : 5000})
car3 = Car('Audi', {'color' : 'silver','horsepower' : 300,'price' : 7000})


# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))


print(car1._company == car2._company)
print(car1 is car2)

# dir &__dict__ 확인
print(dir(car1))
print(dir(car2))

print()
print()

print(car1.__dict__)
print(car2.__dict__)

# Doctring
print(Car.__doc__)
print()

# 실행
car1.detail_info() 
Car.detail_info(car1)
car2.detail_info()
Car.detail_info(car2) 

# 에러
# Car.detail_info() 에러남
Car.detail_info(car2) # 클래스 이름으로 접근했을 때에는 인자를 넣어줘야한다. car2 = self인자

# 비교
print(car1.__class__, car2.__class__)
print(Car.__class__)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))
print(id(car1.__class__) == id(car2.__class__) == id(car3.__class__)) # True
 
# 공유확인
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count) # 정석

del car2
# 삭제 확인
print(car1.car_count) # 인스턴스 변수는 인스턴스 이름으로 접근
print(Car.car_count) # 클래스 변수는 클래스 이름으로 접근 하여야한다.

# 인스턴스 네임스페이스에 없면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색후 -> 상위(클래스 변수, 부모 클래스))
# self._company = company # instans 변수
        #self._details = details
        #self.car_count = 10  car_count가 dir에 포함되어있어서 car1.car_count는 10이 나옴 => 없으면 (상위)클래스 변수에서 찾아옴 => 그래도 없으면 에러
        #Car.car_count += 1

# print(car1.car_count) <-
# print(Car.car_count)