import time
print(time.time())

print()
print()


print(time.localtime(time.time()))

print()
print()


print(time.asctime(time.localtime(time.time())))
print(time.ctime())

print()
print()


print(time.strftime('%x', time.localtime(time.time())))

print()
print()


print(time.strftime('%c', time.localtime(time.time())))

print()
print()


#sleep1.py
import time
for i in range(10):
    print(i)
    time.sleep(0.1)

print()
print()


import calendar
print(calendar.calendar(2015))

print()
print()
print()
print()



calendar.prcal(2020)

print()
print()
print()
print()


calendar.prmonth(2015, 12)

print()
print()
print()
print()

print(calendar.monthrange(2015,12))


import time

print(time.strftime("%Y/%m/%d %H:%M:%S"))
