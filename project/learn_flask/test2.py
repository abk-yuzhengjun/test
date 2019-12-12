import datetime


def demo(function):
    status = {}

    def wrapper(*args):
        if args not in status:
            status[args] = function(*args)
        return status[args]

    return wrapper


@demo
def fib(i):
    if i < 2:
        return 1
    else:
        return fib(i - 1) + fib(i - 2)


f1 = 1
f2 = 2
f3 = 4
f4 = 8

fib2 = lambda n: n if n <= 2 else fib2(n - 1) + fib2(n - 2)
fib4 = lambda n: n if n < 2 else 2 * fib4(n - 1)
print(fib2(30))

l1 = [1, 2, 3, 4, 3, 4, 123, 32, 4, 23, 3, 4, 2, 4, 56, 7, 8]
l2 = []
[l2.append(i) for i in l1 if i in l1 and i not in l2]
print(l2)


def fib3(n):
    a, b = 0, 1
    for x in range(30):
        a, b = b, a + b
    return b


now1 = datetime.datetime.now()
print(fib(300))
print(fib3(30))
now2 = datetime.datetime.now()
print(now2 - now1)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def swapPairs(self, head):
        if head is not None and head.next is not None:
            next = head.next
            head.next = self.swapPairs(next.next)
            next.next = head
            return next
        return head


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((high - low) / 2) + low  # 避免(high + low) / 2溢出
        guess = list[mid]
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return mid
    return None


mylist = [1, 3, 5, 7, 9]
print(binary_search(mylist, 3))


# 快速排序
def quickSort(list):
    if len(list) < 2:
        return list
    mid = list[0]
    lessMid = [i for i in list[1:] if i < mid]
    moreMid = [i for i in list[1:] if i >= mid]
    final = quickSort(moreMid) + [mid] + quickSort(lessMid)
    return final


# 冒泡排序 最大的放到最后一位，执行n次
# 我，最小的放到第一位，执行n次
def bubbleSort(list):
    if len(list) < 2:
        return list
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    print(list)
    return list


def selectSort(relist):
    len_ = len(relist)
    for i in range(len_):
        min_index = i
        for j in range(i + 1, len_):  # 这个循环会找到值比第i个索引所代表值小的索引
            if relist[j] < relist[min_index]:
                min_index = j
        relist[i], relist[min_index] = relist[min_index], relist[i]  # 互换两个索引位置
    return relist


# 选择排序
def selectSort2(list):
    if len(list) < 2:
        return list
    for i in range(len(list)):
        tempmin = i
        for j in range(i + 1, len(list)):
            if list[j] < list[tempmin]:
                tempmin = j
        list[i], list[tempmin] = list[tempmin], list[i]
    return list


print(quickSort(
    [1, 235, 346, 4, 363, 45, 345, 325, 23, 45, 234, 6, 4673, 2, 5342, 67, 5436, 7, 5, 8, 567, 85, 8, 5, 3, 56, 32, 5,
     235, 32, 5, 4325, 43, 6, 3, 63, 6, 36, 3, 53, 454, 3, 534, 5, 345, 34, 5, 43]))

bubbleSort(
    [1, 235, 346, 4, 363, 45, 345, 325, 23, 45, 234, 6, 4673, 2, 5342, 67, 5436, 7, 5, 8, 567, 85, 8, 5, 3, 56, 32, 5,
     235, 32, 5, 4325, 43, 6, 3, 63, 6, 36, 3, 53, 454, 3, 534, 5, 345, 34, 5, 43])

print(selectSort(
    [1, 235, 346, 4, 363, 45, 345, 325, 23, 45, 234, 6, 4673, 2, 5342, 67, 5436, 7, 5, 8, 567, 85, 8, 5, 3, 56, 32, 5,
     235, 32, 5, 4325, 43, 6, 3, 63, 6, 36, 3, 53, 454, 3, 534, 5, 345, 34, 5, 43]))

print(selectSort2(
    [1, 235, 346, 4, 363, 45, 345, 325, 23, 45, 234, 6, 4673, 2, 5342, 67, 5436, 7, 5, 8, 567, 85, 8, 5, 3, 56, 32, 5,
     235, 32, 5, 4325, 43, 6, 3, 63, 6, 36, 3, 53, 454, 3, 534, 5, 345, 34, 5, 43]))

__author__ = 'abcdefg' \
             'hijklmn' \
             'opq rst' \
             'uvw xyz_'
if __author__ == 'abcdefg' \
                 'hijklmn' \
                 'opq rst' \
                 'uvw xyz_':
    print('answer is : j')
    pass


class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            print('left is not None')
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            print('right is not None')
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('0')
r.insertLeft('1')
r.insertRight('2')
r.getLeftChild().insertLeft('3')

r.getLeftChild().insertRight('4')
r.getRightChild().insertLeft('5')
r.getRightChild().insertRight('6')
r.getLeftChild().getLeftChild().insertLeft('7')
r.getLeftChild().getLeftChild().insertRight('8')
r.getLeftChild().getRightChild().insertLeft('9')


# 中序遍历:遍历左子树,访问当前节点,遍历右子树
def mid_travelsal(root):
    if root.getLeftChild() is not None:
        mid_travelsal(root.getLeftChild())
    # 访问当前节点
    print(root.getRootVal())
    if root.getRightChild() is not None:
        mid_travelsal(root.getRightChild())


# 前序遍历:访问当前节点,遍历左子树,遍历右子树
def pre_travelsal(root):
    print(root.getRootVal())
    if root.getLeftChild() is not None:
        pre_travelsal(root.getLeftChild())
    if root.getRightChild() is not None:
        pre_travelsal(root.getRightChild())


# 后序遍历:遍历左子树,遍历右子树,访问当前节点
def post_trvelsal(root):
    if root.getLeftChild() is not None:
        post_trvelsal(root.getLeftChild())
    if root.getRightChild() is not None:
        post_trvelsal(root.getRightChild())
    print(root.getRootVal())


print('===============中序=====================')
mid_travelsal(r)
print('=====================================')
print('================前序=====================')
pre_travelsal(r)
print('=====================================')
print('================后序=====================')
post_trvelsal(r)
print('=====================================')

# 动态规划DP
w = [0, 1, 4, 3, 1]
p = [0, 1500, 3000, 2000, 2000]
n = len(w) - 1
m = 4
x = []
v = 0
optp = [[0 for col in range(m + 1)] for raw in range(n + 1)]


def knapsack_dynamic(w, p, n, m, x):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if j >= w[i]:
                optp[i][j] = max(optp[i - 1][j], optp[i - 1][j - w[i]] + p[i])
            else:
                optp[i][j] = optp[i - 1][j]

    return optp[n][m]


def fib(n):
    global m
    if n < 2:
        return n
    elif n in m:
        return m[n]
    else:
        result = fib(n - 1) + fib(n - 2)
        m[n] = result
        return result


print(knapsack_dynamic(w, p, n, m, x))

# 双核CPU 单核一秒1k  n个任务放入CPU， 如何放时间最短
#     总任务数:  n
# 单个任务时间:  length[i]
# 相差时间: time[n]

coins = [2, 3, 5]
list = [x for x in range(3, 20)]
res = [0 for x in range(30)]


def getMin(*args):
    print(args, type(args))
    if args:
        minvalue = args[0]
    else:
        return 0
    for i in args:
        if i < minvalue and i != 0:
            minvalue = i
    return minvalue


import random

# 一个序列有 N 个数：A[1],A[2],…,A[N]，求出最长非降子序列的长度
a = []
for i in range(30):
    a.append(random.randint(1, 30))
print(a)
res[0] = 1
res[1] = 1
n = 30
curlen = 1
for i in range(1, 30):
    if a[i] < a[i - 1]:
        res[i] = res[i - 1]
        curlen = 1
    else:
        if curlen >= res[i - 1]:
            res[i] = res[i - 1] + 1
        else:
            res[i] = res[i-1]
        curlen += 1

print(res)

# 硬币问题

# res[0] = 0
# res[1] = 0
# res[2] = 1
# for i in list:
#     if i >= 5:
#         res[i] = getMin(res[i - 2], res[i - 3], res[i - 5]) + 1
#     else:
#         res[i] = getMin(res[i - 2], res[i - 3]) + 1

print(res)


def lis(*args,num=1):
    d = [0]*len(args)
    len_num = 1
    for i in range(len(args)):
        d[i] = 1
        for j in range(i):
            if args[j] <= args[i] and d[i] < d[j] + 1:
                d[i] = d[j] + 1
            if d[i] > len_num:
                len_num = d[i]

    return len_num

print(lis(5,3,4,8,6,7));

# 最小时间
