import os

print("내 시스템의 환경 변수값을 알고 싶을 때__________________________")

print(os.environ)

print("__________________________")

print('''os.environ['PATH']''')

os.environ['PATH']

print("디렉터리 위치 변경하기__________________________")

print(os.chdir("C:\WINDOWS"))

print("디렉터리 위치 돌려받기__________________________")

print(os.getcwd())

print("시스템 명령어 호출하기__________________________")

os.system("dir")

print("실행한 시스템 명령어의 결괏값 돌려받기__________________________")

f = os.popen("dir")

print(f.read())


'''
기타 유용한 os 관련 함수
os.mkdir(디렉터리) 디렉터리를 생성한다.
os.rmdir(디렉터리) 디렉터리를 삭제한다. 단, 디렉터리가 비어있어야 삭제가능
os.unlink(파일) 파일을 지운다.
os.rename(src, dst) src라는 이름의 파일을 dst라는 이름으로 바꾼다.
'''