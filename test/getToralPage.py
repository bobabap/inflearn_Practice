def getToralPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(getToralPage(37, 10))
