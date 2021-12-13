'''while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.'''
# 내가 한거
while True:
    mul = []
    for i in range(1, 1001):
        if i % 3 == 0:
            mul.append(i)
    print(sum(mul))
    break

# 정답
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
        result += i
    i += 1

print(result)