#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import copy
from copy import deepcopy
import os


class Student:
    name = None

    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self):
        pass

    def __str__(self):
        return self.name


import functools


def log(text):
    def decorate(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            print('%s before func' % text)
            res = function(*args, **kwargs)
            print('%s after func' % text)
            return res

        return wrapper

    return decorate


@log('param')
def func(str):
    print('execute func %s' % str)

# 装饰器单例
def singleton(cls, *args, **kwargs):
    instance = {}

    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return _singleton


# 使用装饰器实现的单例模式

# 邮箱正则表达式
# r'^[0-9a-zA-Z_]{0, 19}@[0-9a-zA-Z]{0-13}\.(com|net|cn)$'
# r'^[a-zA-Z0-9_]{1,19}@[a-zA-Z0-9]{1,19}\.(net|cn|com)$'


@singleton
class test_singleton(object):
    name = None

    def __init__(self):
        self.sum = 0

    def add(self, name):
        self.name = name


# 进程间通信方式
#

class CCP(object):
    """封装单例类，用于统一的发送短信验证码"""
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._instance = super(CCP, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def send_sms_msg(self, name):
        self._singleton = name


def checkHuiwen(str):
    if len(str) == 1:
        return 1
    elif len(str) == 2 and str[0] == str[1]:
        return 1
    elif len(str) == 0:
        return 0
    else:
        if str[0] == str[-1]:
            return checkHuiwen(str[1:-1])
        else:
            return 0


def testGlobal():
    global a
    a = 10
    while True:
        a += 1
        if a > 20:
            break


testGlobal()

a += 1

print(a)

L1 = ['AsiA', 'America', 18, None, 'test']

L2 = [x.lower() for x in L1 if isinstance(x, str)]

print(L2)

a = [1, 2, 5, 7, 6, 8, 6, 5, 3, 3, 4, 2, 3, 7, 9, 0]

a.sort()
print(a)
print(a[1:-1])
length = len(a)
print(a[int(length / 2) - 1])
print(a[int(length / 2)])
print(3 / 2)

path = os.walk(r'D:\AFS\AFS-webserver')

for i in path:
    print(i[0])
    print(i[1])
    print(i[2])
    print(i, type(i))


# select name and password from user

class A:
    name = None

    def foo(self, x):
        print('executing foo(%s,%s)' % (self, x))

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    @classmethod
    def class_foo(cls, x):
        print('executing class_foo(%s,%s)' % (cls, x))

    @staticmethod
    def static_foo(x):
        print('executing static_foo(%s)' % x)


a = A()
a.foo('123')
a.class_foo('1234')
a.static_foo('12345')
a.setName('yuzhengjun')
print(A.name)
b = A()
b.setName('jiangjunjun')
print(A.name, a.getName())


def demo(function):
    status = {}
    def wrapper(*args):
        if args not in status:
            status[args] = function
        return status[args]
    return wrapper


@demo
def fib(i):
    if i < 2:
        return 1
    else:
        return fib(i-1)+fib(i-2)


class Person:
    name = []


p1 = Person()
p2 = Person()
p1.name.append('123')
p2.name.append('234')
print(p1.name, p2.name, Person.name)

hash = {'name': 'yuzhengjun'}
li = ['name', 18]
tuple = (1, 2, 3)
print(li, hash, tuple)
name = (1, 2, 3)
print('this is {}'.format(name))


# __new__
class singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(singleton, cls)
            cls._instance = orig.__new__(cls)
            print('not hasattr')
        print('attr over')
        return cls._instance

    def __init__(self):
        print('singleton init')


class myclass(singleton):
    a = 1

    def __init__(self):
        print('myclass init')
        myclass.a += 1
        print(myclass.a)


my = myclass()
my2 = myclass()
print(my.a)
print(my2.a)



# 共享属性
class borg(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(borg, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob


class myclass2(borg):
    a = 2


if __name__ == '__main__':
    cls1 = test_singleton()
    cls1.add('cls1')
    cls2 = test_singleton()
    cls2.add('cls2')
    cls3 = test_singleton()
    cls3.add('cls3')
    print(cls1)
    print(cls2)
    print(cls3)
    print(cls1.name)
    print(cls2.name)
    print(cls3.name)
    a = []
    b = [a]
    a.append(b)
    print(a, b)
    c = range(1, 10)
    print(c, type(c))
    c1 = CCP()
    c1.send_sms_msg('c1')
    c2 = CCP()
    c2.send_sms_msg('c2')
    c3 = CCP()
    c3.send_sms_msg('c3')
    print(c1)
    print(c2)
    print(c3)
    str = [' ', 'ab', 'cd', 'ef', 'op', ' ']
    str2 = ' '.join(str)
    print(str2, type(str2))
    print(str2.strip())
    # print('%s = %s' % (str, checkHuiwen(str)))
    L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
    a = list(map(lambda x:x * x + 1,range(1,20)))
    print(L)
    print(a)
