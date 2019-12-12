import queue

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

height = 1.75
weight = 80.5
bmi = 80.5 / 1.75 ** 2

if bmi > 27:
    print('A')
elif 24 <= bmi <= 27:
    print('B')
elif 19 <= bmi <= 24:
    print('C')
else:
    print('D')
print(bmi)

L1 = {'123': 123}
L1['124'] = 124
L1['125'] = 125
if '123' in L1:
    print('\'123\' in')
else:
    print('not in')
print(L1.get('123'))
print(L1.get('124'))

s = {1, 2, 3, 4}
s.add(5)
s.add(6)
s.remove(5)
print(s)
n1 = 255
n2 = 1000
print(hex(n1), type(hex(n1)))
print(hex(n2), type(hex(n2)))


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


import math


def quadratic(a, b, c):
    print(-b)
    if b * b - 4 * a * c < 0:
        return
    else:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (a * 2)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (a * 2)
        return x1, x2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


def quickSort(list):
    if len(list) < 2:
        return list
    mid = list[0]
    lessMid = [i for i in list[1:] if i <= mid]
    moreMid = [i for i in list[1:] if i > mid]
    final = quickSort(lessMid) + [mid] + quickSort(moreMid)
    return final


print(quickSort(
    [1, 4214, 235, 346, 345, 34, 532, 23, 42, 34, 1, 23, 1, 3, 23, 5, 32, 4, 32, 4, 23, 4, 234, 2, 34, 23, 423, 4, 23,
     42, 3, 5, 56, 76, 86, 9, 80, 8, -9]))


def f1(a,b,c=0,*args,**kwargs):
    print(a,b,c,args,kwargs)

f1(1,2)
f1(1,2,3)