numbers = [1, 2, 3, 4, 5]
result = []

for n in numbers:
    if n % 2 == 1:
        result.append(n*2)


# list comprehension
numbers = [1, 2, 3, 4, 5]

result = [n * 2 for n in numbers if n % 2 == 1]
print(result)