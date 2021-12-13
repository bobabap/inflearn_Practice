'''while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.'''

# 내 답
star = 0
while True:
    for i in range(5):
        star += 1
        print(star * ('*'))
    break

# 정답
i = 0
while True:
    i += 1 # while문 수행 시 1씩 증가
    if i > 5: break     # i 값이 5보다 크면 while문을 벗어난다.
    print('*' * i)     # i 값 개수만큼 *를 출력한다.