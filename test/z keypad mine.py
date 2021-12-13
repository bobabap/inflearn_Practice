import numpy as np

left_start = [1, 0]
right_start = [2, 3]
now = [0, 1]

left_distance = 0
right_distance = 0

for a, b, c in zip(left_start, right_start, now):
                left_distance += abs(a-c)
                right_distance += abs(b-c)

print('a, b, c : ', a, b, c)

left_start = [1, 0]
now = [0, 1]
u = np.array(left_start)
v = np.array(now)
w = u - v
left_d = abs(w)
print(left_d)

right_start = [2, 3]
now = [0, 1]
x = np.array(right_start)
v = np.array(now)
p = x - v
right_d = abs(p)
print(right_d)

result = w - p
print(result)


left_start = np.array([1, 0])
right_start = np.array([2, 3])
now = np.array([0, 1])

print()

d = np.array(list(zip(left_start,right_start,now)))
print(d)