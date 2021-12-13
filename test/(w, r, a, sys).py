f = open("C:/doit/새파일.txt", 'w')
f.close()


# writedata.py
f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close

for i in range(1, 11):
    data = "%d번째 줄입니다. \n" % i
    print(data)

# readline_test.py
f = open("C:/doit/AI 부트캠프.txt", 'r', encoding='utf_8')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()

print()
print()

f = open("C:/doit/새파일.txt", 'r')
line = f.readlines()
print(line)
f.close()

print()
print('readline_all.py')
# readline_all.py
f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readlines()
    if not line: break
    print(line)
f.close

print()
print('''readlines 함수 사용하기''')
'''readlines 함수 사용하기'''
f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()


print()
print("줄바꿈문자 제거")
f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()

print()
print('''read 함수 사용하기''')
'''read 함수 사용하기'''
f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()


print()
print('''파일에 새로운 내용 추가하기''')
# adddata.py
f = open("C:/doit/새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


print()
print('''with문과 함께 사용하기''')
'''with문과 함께 사용하기'''
f = open("C:/doit/foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

print()
with open("C:/doit/foo.txt", "w") as f:
    f.write("Life is too short, you need python")


'''IDLE 로 doit파일에 저장하고 CMD로 실행

C:\doit>python sys2.py life is too short, you need python
LIFE IS TOO SHORT, YOU NEED PYTHON
C:\doit>python sys1.py sys1.py aaa bbb ccc
sys1.py
aaa
bbb
ccc

C:\doit>python sys2.py life is too short, you need python
LIFE IS TOO SHORT, YOU NEED PYTHON
'''
# #sys1.py
# import sys

# args = sys.argv[1:]
# for i in args:
#     print(i)


# #sys2.py
# import sys
# args = sys.argv[1:]
# for i in args:
#     print(i.upper(), end=' ')

print()
print('''단어 수정하기''')
# 전체를 읽은다음
f = open("text.txt", 'r')
body = f.read()
f.close()
# 수정
body = body.replace('java', 'python')
f = open("text.txt", 'w')
f.write(body)
f.close()