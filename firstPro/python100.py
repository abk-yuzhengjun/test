def func24(num):
    f1 = 1.0
    f2 = 2.0
    res = 0.0
    for x in range(num):
        res = res + f2 / f1
        f2 = f1 + f2
        f1 = f2 - f1
    print(res)


def jiecheng(param):
    res = 1
    for i in range(1, param + 1):
        res = res * i
    return res


def func25(num):
    res = 0
    for i in range(1, num + 1):
        res += jiecheng(i)
    print(res)


def func26(num):
    if num == 1:
        return 1
    return func26(num - 1) * num


def func27(str):
    new_str = ''
    for i in range(len(str) - 1, -1, -1):
        new_str = new_str + str[i]
    print(new_str)


def func28():
    pass


def func29(num):
    a = int(num / 10000)
    b = int(num / 1000) - a * 10
    c = int(num / 100) - a * 100 - b * 10
    d = int(num / 10) - a * 1000 - b * 100 - c * 10
    e = num % 10
    print(a, b, c, d, e)


def func30(num):
    print([x*x for x in range(9)])


def func31():
    res = ''
    word1 = input('please input:')
    if word1 == 'M':
        res = 'Monday'
    elif word1 == 'W':
        res = 'Wednesday'
    elif word1 == 'f':
        res = 'Friday'
    elif word1 == 'T':
        word2 = input('please input second word:')
        if word2 == 'u':
            res = 'Tuesday'
        elif word2 == 'h':
            res = 'Thursday'
        else:
            print('the second word is error!')
    elif word1 == 'S':
        word2 = input('please input second word:')
        if word2 == 'a':
            res = 'Saturday'
        elif word2 == 'u':
            res = 'Sunday'
        else:
            print('the second word is error!')
    else:
        print('the first word is error!')

    if res == '':
        return
    print('you want to input ', res)


def func32(list):
    print(list[::-1])
    return list[::-1]


def func33(list):
    s1 = ':'.join(str(i) for i in list)
    print(s1)


def func34():
    pass


def func35():
    print(123)


def func36():
    pass


def func37():
    profit = 1.1
    for i in range(20):
        print(profit + i * 0.01)
        sum = 0
        for j in range(15):
            sum = sum * (profit + i * 0.01) + 10
        print(sum)


def func38():
    pass


def func39():
    pass


def func40():
    pass


def func41():
    pass


def func42():
    pass



if __name__ == '__main__':
    # func24(20)
    # func25(20)
    # func26(5)
    # func27('this is a string')
    # func28()
    # func29(87651)
    # func30()
    # func31()
    # func32([1, 3, 5, 7, 9])
    # func33('string')
    # func34()
    # func35()
    # func37()
    func37()
