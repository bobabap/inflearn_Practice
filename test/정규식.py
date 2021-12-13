# 정규식
import re # Regular Expressions
p = re.compile('[a-z]+')

m = p.match("python")
print(m)

print('--------------------------------')

m = p.match("3 python")
print(m)

print('--------------------------------')

# p = re.compile('정규표현식')
# m = p.match( 'string goes here' )
# if m:
#     print('Match found: ', m.group())
# else:
#     print('No match')


print('--------------------------------')

m = p.search("python")
print(m)

print('--------------------------------')

m = p.search("3 python")
print(m)

print('--------------------------------')

result = p.findall("life is too short")
print(result)

print('--------------------------------')

result = p.finditer("life is too short")
print(result)

for r in result: print(r)

print('--------------------------------')


p = re.compile('[a-z]+')
m = p.match("python")
# 축약형
m = re.match('[a-z]+', "python")