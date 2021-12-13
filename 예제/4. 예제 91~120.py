print("파이썬 딕셔너리-------------------------------------091 딕셔너리 생성")
# 091 딕셔너리 생성
'''아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라.
   딕셔너리의 이름은 inventory로 한다.
   
이름	가격	재고
메로나	300	20
비비빅	400	3
죠스바	250	100
'''
inventory = {"메로나" : [300, 20],
             "비비빅" : [400, 3],
             "죠스바" : [250, 100]}
print(inventory)

inventory = \
{
    "메로나" : [300, 20],
    "비비빅" : [400, 3],
    "죠스바" : [250, 100]
}


print("-------------------------------------092 딕셔너리 인덱싱")
# 092 딕셔너리 인덱싱
'''inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.'''
print(inventory["메로나"][0],'원')



print("-------------------------------------093 딕셔너리 인덱싱")
# 093 딕셔너리 인덱싱
'''inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.'''
print(inventory["메로나"][1],'개')


print("-------------------------------------094 딕셔너리 추가")
# 094 딕셔너리 추가
'''inventory 딕셔너리에 아래 데이터를 추가하라.

이름	가격	재고
월드콘	500	7
'''
inventory['월드콘'] = [500,7]
print(inventory)


print("-------------------------------------095 딕셔너리 keys() 메서드")
# 095 딕셔너리 keys() 메서드
'''다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.'''
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecreamkey = list(inventory)
print(icecreamkey) # 내 답
# 정답
ice = list(icecream.keys())
print(ice)


print("-------------------------------------096 딕셔너리 values() 메서드")
# 096 딕셔너리 values() 메서드
'''다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.'''
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.values())
print(ice)


print("-------------------------------------097 딕셔너리 values() 메서드")
# 097 딕셔너리 values() 메서드
'''icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.'''
총합 = sum(icecream.values())
print(총합) # 내 답
# 정답
print(sum(icecream.values()))


print("-------------------------------------098 딕셔너리 update 메서드")
# 098 딕셔너리 update 메서드
'''아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.'''
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
# icecream['팥빙수'] = 2700
# icecream['아맛나'] = 1000
# print(icecream) # 내답 분명 아닐거야 역시
# 정답
icecream.update(new_product)
print(icecream)


print("------------------------------------- 099 zip과 dict")
# 099 zip과 dict
'''아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로
   result 이름의 딕셔너리로 저장한다.'''
# keys = ("apple", "pear", "peach")
# vals = (300,250,400)

# # result = zip (keys, vals)
# # print(type(result), dict(result)) # 내답 type이 zip으로 됨 그래서 틀림
# # 정답
# result = dict(zip(keys, vals))
# print(result)


print("------------------------------------- 100 zip과 dict")
# 100 zip과 dict
'''date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.'''
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date,close_price))
print(close_table)


print("파이썬 분기문------------------------------------- 101")
# 101
'''파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?'''
# bool 타입

print("------------------------------------- 102")
# 102
'''아래 코드의 출력 결과를 예상하라
print(3 == 5)
'''
# False


print("------------------------------------- 103")
# 103
'''아래 코드의 출력 결과를 예상하라
print(3 < 5)
'''
# True


print("------------------------------------- 104")
# 104
'''아래 코드의 결과를 예상하라.
x = 4
print(1 < x < 5)
'''
# True

print("------------------------------------- 105")
# 105
'''아래 코드의 결과를 예상하라.
print((3 == 3) and (4 != 3))'''
# True

print("------------------------------------- 106")
# 106
'''아래 코드에서 발생하는 원인에 대해 설명하라.
print(3 => 4)
'''
#  => 가아니고 >= 이다? 가 아니고 지원하지 않는 형식이다


print("------------------------------------- 107")
# 107
'''아래 코드의 출력 결과를 예상하라.
if 4 < 3:
    print("Hello World")'''
# False 가 아니고 아무 결과도 출력되지 않음 if문이기 때문에


print("------------------------------------- 108")
# 108
'''아래 코드이 출력 결과를 예상하라.
if 4 < 3:
    print("Hello World")
else:
    print("Hi, There")
'''
# Hi, There

print("------------------------------------- 109")
# 109
'''아래 코드의 출력 결과를 예상하라.
if True :
    print("1")
    print("2")
else :
    print("3")
print(4)

124 가 아니고
1
2
4
'''

print("------------------------------------- 110")
# 110
'''아래 코드의 출력 결과를 예상하라.
if True:
    if false:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")

3
5 딩동뎅동
'''

print("------------------------------------- 111")
# 111
'''사용자로부터 입력받은 문자열을 두 번 출력하다.
   아래는 사용자가"안녕하세요"를 입력한 경우의 출력 결과이다.
>> 안녕하세요
안녕하세요안녕하세요'''
# 이거 왜 기억안나
# user = input("입력:")
# print(user * 2)


print("------------------------------------- 112")
# 112
'''사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
>> 숫자를 입력하세요: 30
40
'''
# num = input('숫자를 입력하세요:')
# print(int(num) + 10)


print("------------------------------------- 113")
# 113
'''사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.'''
# x = int(input('정수 x:'))
# if (x%2 == 1):
#     print("홀수입니다")

# else: print("짝수입니다") # 넷상 답
# # 정답
# user = input("홀?짝?")
# if int(user) % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")


print("------------------------------------- 114")
# 114
'''사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라.
   단 사용자가 입력한 값과 20을 더한 값이 255를 초과하는 경우 255를 출력해야한다.'''
# user = input("한계선은 255입니다 값을입력하십시오 :")
# if int(user) < 236:
#     print(int(user)+20)
# else:
#     print(255) # 내답

# # 정답
# user = input("입력값: ")
# num = 20 + int(user)
# if num > 255:
#     print(255)
# else:
#     print(num)


print("------------------------------------- 115")
# 115
'''사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라.
 단 출력 값의 범위는 0~255이다.
 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우
  255를 출력해야 한다.'''
'''
>> 입력값: 200
출력값: 180
>> 입력값: 15
출력값: 0
'''
# user = input("입력값: ")
# num = int(user) - 20
# if num > 255:
#     print(255)
# elif num < 0:
#     print(0)
# else:
#     print(num)


print("------------------------------------- 116")
# 116
'''사용자로부터 입력 받은 시간이 정각인지 판별하라.'''
# usertime = input("현재시간: ")

# if usertime[-2:] == "00":
#     print('정각입니다.')
# else:
#     print('정각이 아닙니다.')
# #어렵네,,


print("------------------------------------- 117")
# 117
'''사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라.
   포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.'''

# fruit = ["사과", "포도", "홍시"]
# user = input("좋아하는 과일은? ")
# if user in fruit:
#     print('정답입니다.')
# else:
#     print('오답입니다.')

print("------------------------------------- 118")
# 118
'''투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이
   투자 경고 종목이라면 '투자 경고 종목입니다.'를 아니면 "투자 경고 종목이 아닙니다."
   를 출력하는 프로그램을 작성하라.'''
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# 종목 = input('종목을 입력하세요: ')
# if 종목 in warn_investment_list:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")


print("------------------------------------- 119")
# 119
'''아래와 같이 fruit 딕셔너리가 정의되어 있다. 
   사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면
  "정답입니다"를 아닐 경우 "오답입니다" 출력하라.'''
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

# user = input("제가좋아하는계절은: ")
# if user in fruit:
#     print('정답입니다.')
# else:
#     print('오답입니다.')


print("------------------------------------- 120")
# 120
'''아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이
딕셔너리 값(value)에 포함되었다면 "정답입니다"를 아닐경우 "오답입니다"를 출력하라.'''
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("좋아하는과일은? ")
# if user in fruit.values(): # () 이거 중요하네
#     print('정답입니다.')
# else:
#     print('오답입니다.')
