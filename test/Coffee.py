coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
        print("남은 커피의 양은 %d개 입니다." % coffee)
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break


''' while True:
     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
'''
# if 문 한줄작성법
# score = 60
# message = print("success") if score >= 60 else print("failure")
