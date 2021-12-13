
'''
10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
1000미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
입력 받는 값은 1부터 999까지
출력하는 값은 3의 배수와 5의 배수의 총합
생각해 볼 것은
    1. 3의 배수와 5의 배수는 어떻게 찾지
    2. 3의 배수와 5의 배수가 겹칠 때는 어떻게 하지
'''
    


result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)