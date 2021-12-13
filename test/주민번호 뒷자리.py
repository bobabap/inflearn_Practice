data = """park 800905-1049118
kim 700905-1059119
""" # 첫 문자 앞 자동enter 끝 문자 뒤 자동enter
            # park 800905-*******
result = [] # kim 700905-*******
for line in data.split("\n"): # park 800905-1049118 
    word_result = []          # kim 700905-1059119
    for word in line.split(" "): # park 800905-1049118 kim 700905-1059119
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit(): # isdigit => 문자열의 모든 문자가 숫자일 때 True를 반환 <-> false
            word = word[:6] + "-" + "*******"
        word_result.append(word)          # ['']
    result.append(" ".join(word_result))  # ['park', '800905-*******']
print("\n".join(result))                  # ['kim', '700905-*******']
                                          # ['']

# 정규식
import re

data = """
park 800905-1049118
kim 700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

