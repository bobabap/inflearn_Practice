'''# myargv
import sys

numbers = sys.argv[1:] # 파일이름을 제외한 명령 행의 모든 것


result = 0
for number in numbers:
    result += int(number)
print(result)

'''