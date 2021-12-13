a = "{{ and }}".format()
print(a)

(a, b) = 'python', 'life'
print(a)
print(b)

a = (1,2,3)
print(a+(4,))

c = [1, 3, 5, 4, 2]
c.sort()
c.reverse()
print(c)


a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

a = {'A':90, 'B':80, 'C':70}
print(a["B"])
result = a.pop('B')
print(a)
print(result)

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
result = set(a)
b = list(result)
print(b)

a = b = [1, 2, 3]
a[1] = 4
print(b)