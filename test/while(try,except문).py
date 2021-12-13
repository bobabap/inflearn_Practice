t = "ABCDEFGHIJKLMNOPQRSTUWXYZ"

w = iter(t) # '__next__',

while True:
    try:
        print(next(w))
    except StopIteration as e:
        break