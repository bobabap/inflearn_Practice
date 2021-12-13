print("-------------------------------------031 문자열 합치기")
# 031 문자열 합치기
'''아래 코드의 실행 결과를 예상해보세요.'''
a = "3"
b = "4"
print(a + b)
# 답 34

print("-------------------------------------032 문자열 곱하기")
# 032 문자열 곱하기
'''아래 코드의 실행 결과를 예상해보세요.'''
print("Hi" * 3)
# 답 HiHiHi

print("-------------------------------------033 문자열 곱하기")
# 033 문자열 곱하기
'''화면에 '-'를 80개 출력하세요.'''
print('-' * 80)

print("-------------------------------------034 문자열 곱하기")
# 034 문자열 곱하기
'''변수에 다음과 같은 문자열이 바인딩되어 있습니다.'''
t1 = 'python'
t2 = 'java'
'''변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.'''
print((t1 +' '+t2 +' ') * 4) # 내 답
# 정답
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)
# python java python java python java python java

print("-------------------------------------035 문자열 출력")
# 035 문자열 출력
'''변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때
% formatting을 사용해서 다음과 같이 출력해보세요.'''
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print('이름: {} 나이: {}'.format(name1,age1))
print('이름: {} 나이: {}'.format(name2,age2)) # 내 답
# 정답
print('이름: %s 나이: %d' % (name1, age1))
print('이름: %s 나이: %d' % (name2, age2))
'''이름: 김민수 나이: 10
   이름: 이철희 나이: 13'''


print("-------------------------------------036 문자열 출력 위에 내 방식")
# 036 문자열 출력 위에 내 방식
'''문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.'''
print('이름: {} 나이: {}'.format(name1,age1))
print('이름: {} 나이: {}'.format(name2,age2))

print("-------------------------------------037 문자열 출력")
# 037 문자열 출력
'''파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.'''
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")


print("-------------------------------------038 컴마 제거하기")
# 038 컴마 제거하기
'''삼성전자의 상장주식수가 다음과 같습니다.
   컴마를 제거한 후 이를 정수 타입으로 변환해보세요.'''
# ???
상장주식수 = "5,969,782,550"

컴마제거 = 상장주식수.replace(',','')
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))

print("-------------------------------------039 문자열 슬라이싱")
# 039 문자열 슬라이싱
'''다음과 같은 문자열에서 '2020/03'만 출력하세요.'''
분기 = "2020/03(E) (IFRS연결)"
print(분기[:-12]) # 내 답
# 정답
print(분기[:7])


print("-------------------------------------040 strip 메서드")
# 040 strip 메서드
'''문자열의 좌우의 공백이 있을 때 이를 제거해보세요.'''
data = "   삼성전자    "
print(data[3:7]) # 내 답
# 정답
data1 = data.strip()
print(data1)


print("-------------------------------------041 upper 메서드")
# 041 upper 메서드
'''다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.'''
ticker = "btc_krw"
print(ticker.upper()) # 내 답
# 정답
ticker1 = ticker.upper()
print(ticker1)

print("-------------------------------------042 lower 메서드")
# 042 lower 메서드
'''다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.'''
ticker = "BTC_KRW"
ticker2 = ticker.lower()
print(ticker2)
# 또 다른 답
'''ticker = ticker.lower()
   print(ticker)'''


print("-------------------------------------043 capitalize 메서드")
# 043 capitalize 메서드
'''문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.'''
h1 = "hello"
print(h1.capitalize()) # 내 답


print("-------------------------------------044 endswith 메서드")
# 044 endswith 메서드
'''파일 이름이 문자열로 저장되어 있을 때
   endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.'''
file_name = "보고서.xlsx"
# print(file_name.endswith('xlsx','xls')) # 틀림
file_name.endswith("xlsx") # 답?

print(file_name.endswith("xlsx")) # 내 답


print("-------------------------------------045 endswith 메서드")
# 045 endswith 메서드
'''파일 이름이 문자열로 저장되어 있을 때
   endswith 메서드를 사용해서 파일 이름이
   'xlsx' 또는 'xls'로 끝나는지 확인해보세요.'''

file_name = "보고서.xlsx"
file_name.endswith(("xlsx", "xls")) # 답? 아닌거같은데?
print(file_name)
print(file_name.endswith("xlsx" and "xls")) # 내 답


print("-------------------------------------046 endswith 메서드")
# 046 endswith 메서드
'''파일 이름이 문자열로 저장되어 있을 때
   startswith 메서드를 사용해서 파일 이름이
   '2020'로 시작하는지 확인해보세요.'''
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))


print("-------------------------------------047 split 메서드")
# 047 split 메서드
'''다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.'''
a = "hello world"
a.split() # 답
print(a)

print(a.split(' ')) # 내 답


print("-------------------------------------048 split 메서드")
# 048 split 메서드
'''다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.'''
ticker = "btc_krw"
ticker.split("_")
print(ticker) # 답

print(ticker.split("_")) # 내 답 틀림


print("-------------------------------------049 split 메서드")
# 049 split 메서드
'''다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.'''
date = "2020-05-01"
date.split("-")
print(date) # 정답


print("-------------------------------------050 rstrip 메서드")
# 050 rstrip 메서드
'''문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.'''
data = "039490     "
print(data.rstrip()) # 내 답

data = data.rsplit() # 답
print(data) 


print("-------------------------------------051 리스트 생성")
# 051 리스트 생성
'''2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다.
   영화 제목을 movie_rank 이름의 리스트에 저장해보세요.
    (순위 정보는 저장하지 않습니다.)
    1. 닥터 스트레인지
    2. 스플릿
    3. 럭키
    '''
movie_rank = ['닥터 스트레인지','스플릿','럭키']
print(movie_rank)


print("-------------------------------------052 리스트에 원소 추가")
# 052 리스트에 원소 추가
'''051의 movie_rank 리스트에 "배트맨"을 추가하라.'''
movie_rank.append('배트맨')
print(movie_rank)


print("-------------------------------------053")
# 053
'''movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다.
  "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
  
  리스트의 insert(인덱스, 원소) 메서드를 사용하면
  특정 위치에 값을 끼어넣기 할 수 있습니다.'''

movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,'슈퍼맨') # 인서트 메서드는 인덱스로 접근한다
print(movie_rank) # 정답 기억안났다 이건


print("-------------------------------------054")
# 054
'''movie_rank 리스트에서 '럭키'를 삭제하라.'''
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank.remove('럭키')
# print(movie_rank) # 내 답

# 정답
del movie_rank[3]
print(movie_rank)


print("-------------------------------------055")
# 055
'''movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.'''

'''del을 이용하여 리스트에서 원소를 삭제할 수 있습니다.
   리스트에서 어떤 값을 삭제하면 남은 값들은 새로 인덱싱됩니다.
   따라서 여러 값을 삭제할 때는 어떤 값이 먼저 삭제된 후
   남은 원소들에 대해서 순서를 새로 고려한 후 삭제해야 합니다.'''

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# 정답
# del movie_rank[2]
# del movie_rank[2]
# print(movie_rank)

movie_rank.remove('스플릿')
movie_rank.remove('배트맨')
print(movie_rank) # 내 답


print("-------------------------------------056")
# 056
'''lang1과 lang2 리스트가 있을 때
   lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.'''
'''실행 예:
>> langs
['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']'''
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)


print("-------------------------------------057")
# 057
'''다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)'''
nums = [1, 2, 3, 4, 5, 6, 7]
'''실행 예
max:  7
min:  1
'''
m1 = max(nums)
m2 = min(nums)
print('max: ',m1)
print('min: ',m2) # 내 답
# 정답
print("max: ", max(nums))
print("min: ", min(nums))


print("-------------------------------------058")
# 058
'''다음 리스트의 합을 출력하라.'''
nums = [1, 2, 3, 4, 5]
'''실행 예:
   15
'''
print(sum(nums))


print("-------------------------------------059")
# 059
'''다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.'''
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두",\
 "쫄면", "소시지", "라면", "팥빙수", "김치전"]

print(len(cook))


print("-------------------------------------060")
# 060
'''다음 리스트의 평균을 출력하라.'''

nums = [1, 2, 3, 4, 5]
'''실행 예:
   3.0
'''
average = sum(nums) / len(nums)
print(average) # 이걸 햇갈리냐
