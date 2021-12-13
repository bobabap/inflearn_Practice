# chapter02-01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩
# 차량1

car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color' : 'white'},
    {'horsepower' : 400},
    {'price' : 8000}    
]

# 차량2

car_company_1 = 'Bmw'
car_detail_1 = [
    {'color' : 'black'},
    {'horsepower' : 270},
    {'price' : 5000}    
]

# 차량3

car_company_1 = 'Audi'
car_detail_1 = [
    {'color' : 'silver'},
    {'horsepower' : 300},
    {'price' : 7000}    
]


# 리스트 구조
# 관리하기가 불편
car_company_list = ['Ferrari','Bmw','Audi']
car_detail_list = [
    {'color' : 'white','horsepower' : 400,'price' : 8000},
    {'color' : 'black','horsepower' : 270,'price' : 5000},
    {'color' : 'silver','horsepower' : 300,'price' : 7000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()


# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(key), 키 조회 예외 처리 등

car_dicts = [
{'car_company': 'Ferrari', 'car_detail': {'color' : 'white','horsepower' : 400,'price' : 8000}},
{'car_company': 'Bmw', 'car_detail': {'color' : 'black','horsepower' : 270,'price' : 5000}},
{'car_company': 'Audi', 'car_detail': {'color' : 'silver','horsepower' : 300,'price' : 7000}}
]    


# pop(ket,'default')
del car_dicts[1]
print(car_dicts)

print()
print()

# class 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self): # 사용자 입장에서 출력, print문으로 정보를 확인할때 __str__,  __repr__ 둘이 같이 실행하면 __str__만 실행됌
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self): # 객체 그대로 표현해주고싶을때 개발자 입장에서 엄격한 타입을 인식할수있는
        return 'repr : {} - {}'.format(self._company, self._details)

    def __reduce__(self):
        pass

car1 = car('Ferrari', {'color': 'white','horsepower' : 400,'price' : 8000})
car2 = car('Bmw', {'color' : 'black','horsepower' : 270,'price' : 5000})
car3 = car('Audi', {'color' : 'silver','horsepower' : 300,'price' : 7000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__) # 네임스페이스,속성을 볼수있음
print(car2.__dict__)
print(car3.__dict__)

# 위에 def 없이 print문 실행시 : <__main__.car object at 0x0000019AC723DFD0> 출력
# print(dir(car1)) 한번 출력해 보시게

print()
print()

# 리스트 선언 
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()
print()

# 반복(__str__)
for x in car_list:
    print(repr(x))
    # print(x)






