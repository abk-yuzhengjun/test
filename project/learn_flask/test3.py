# 假设我们有n件物品，分别编号为1, 2...n。其中编号为i的物品价值为vi，它的重量为wi。为了简化问题，假定价值和重量都是整数值。
# 现在，假设我们有一个背包，它能够承载的重量是W。现在，我们希望往包里装这些物品，使得包里装的物品价值最大化，
# 那么我们该如何来选择装的东西呢？


# 首先，构造状态转移方程
# 我们先创建一个二维数组,行：物品种类，列：重量 dp[i][j]含义为 物品种类为i种,最大重量为j
# 方程可得
# 当重量足够装这个物品时，即 j >= w[i]时  dp[i][j] = max(dp[i-1][j - w[i]] + v[i],dp[i-1][j])
# 当不够时，dp[i][j] = dp[i-1][j]


w = [1, 4, 3, 1]    #重量
v = [1500, 3000, 3000, 3000]   #价值
n = 4    #总重量
res = [[0 for col in range(n + 1)] for raw in range(len(v))]


def pack(v, w, n):
    for i in range(len(v)):  #各种物品
        for j in range(n + 1):  #重量
            if j >= w[i]:
                res[i][j] = max(res[i - 1][j], res[i - 1][j - w[i]] + v[i])
            else:
                res[i][j] = res[i - 1][j]

    return res[len(v) - 1][n]


print(pack(v, w, n))

# 一个序列有 N 个数：A[1],A[2],…,A[N]，求出最长非降子序列的长度

# 构造状态转移方程
# 创建一个一维数组dp[i]用来存储当前第i个数据的非降子序列长度
# 定义一个curlen来表示最长的非降子序列长度
# 可得方程
# 如果args[i] >= args[j]，然后比较dp[i] <= dp[j]，那么dp[i] = dp[j] + 1
# 这样比较完j = range(0,i)，就可以得到dp[i]
# 再用curlen存储最长的非降子序列长度

list = [5, 7, 3, 4, 6, 8]


# if a[i]>a[i-1]
# x:  res[i] = res[i-1] + 1
def lis(*args):
    curnum = 1
    res = [0] * len(args)
    print(len(args))
    for i in range(len(args)):
        res[i] = 1
        for j in range(i):
            if args[j] <= args[i] and res[i] < res[j] + 1:
                res[i] = res[j] + 1
            if res[i] > curnum:
                curnum = res[i]
    print(res)
    return curnum


print(lis(5, 7, 3, 4, 6, 8))

import itertools




# 约瑟夫环问题数学解法
# @[TOC]
# # 1.简介
# >问题描述：n个人（编号0~(n-1))，从0开始报数，报到(m-1)的退出，剩下的人继续从0开始报数。求胜利者的编号。
# # 2.思路
# >1.一共n个人，编号为(0~(n-1))，设最后的胜利者为本次编号y的人
# 2.第一次报完数后剩下n-1个人，我们把编号重新排列为(0~(n-2))，设最后的胜利者为本次编号为x的人
# 3.我们可以知道，1中的胜利者y和2中的胜利者x是同一个人
# 4.由3可以得到,y =( x + m ) % n
# 5.由以上可以得到递推公式
# f(1) = 0
# f(i) = (f(i-1) + m) % n
# 其中n为参加游戏的总人数，m为第m个报数，i为当前剩余人数,f(i)为最后一个人的编号


# 3.python代码
def josephus(n,m):
    if n < 2:
        return 0
    f = [0] * (n+1)
    # 注意编号从0开始
    f[1] = 0
    for i in range(2,n+1):
        f[i] = (f[i-1] + m) % n
    return f[n]

print('answer is: ',josephus(41,3))