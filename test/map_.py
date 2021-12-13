def two_times(x):
    return x*2

print(list(map(two_times, [1, 2, 3, 4])))


print(list(map(lambda a: a*2, [1, 2, 3, 4])))