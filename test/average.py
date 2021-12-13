def average(*args):
    
    result = 0
    for i in args:
        result += i
    return result / len(args)


a = average(10, 20, 30, 40, 50)
print(a)