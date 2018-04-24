# 题目描述：
# 有一颗树，非常奇特，有n个节点，由n-1条边连接在一起。
# 树上的每条边都有权值，现在给出Q个询问，每次询问(u,v)路径上所有边的边权最大值.
# 输入
# 第一行一个数N，表示树的大小
# 接下来N-1行，每行三个整数u,v,c，表示u,v之间有一条权值为c的边，输入保证是棵树
# 接下来一行一个整数Q，表示询问个数
# 接下来每行一对整数(u,v)，表示一次查询
# 输出
# 对于每个查询，输出答案

# 样例输入
# 5
# 2 1 3
# 3 2 2
# 4 3 5
# 5 4 1
# 5
# 2 1
# 3 1
# 3 5
# 1 2
# 4 2
#
#
# 样例输出
# 3
# 3
# 5
# 3
# 5

# Hint
# 数据范围：
# 20%的数据保证：1<=N,Q<=1000,|a[i]|<=10^9
# 100%的数据保证：1<=N,Q<=100000,|a[i]|<=10^9」
# - - - - - - - - - - - - - - -
#
# 本题的解题思路用到动态规划，具体为定义一个数组dat[i][j],表示i到j点间最大边的权重
import numpy as np
def func(N, Ws, Qs):
    dat = [[-1 for i in range(N+1)] for j in range(N+1)]
    # print(dat[5][5])
    #step1 构建dat数组dat[i][j] 表示i点到j点间最大边的权重,且根据题目特点我们只考虑i>j的情况
    for W in Ws:
        start = W[0]
        end = W[1]
        weight = W[2]
        dat[start][end] = weight
        sec = start - 1
        for j in range(sec-1, 0, -1):
            if dat[sec][j] > weight:#当前的跟前面的比较
                dat[start][j] = dat[sec][j]
            else:
                dat[start][j] = weight
    #step2 查询,测试要注意若询问的值不是start>end要进行互换,因为dat只记录了start>end的情况
    rtn = []
    for Q in Qs:
        start = Q[0]
        end = Q[1]
        if end > start:
            start, end = end, start
        rtn += [dat[start][end]]
    return rtn

Ws = [[2, 1, 3],
      [3, 2, 2],
      [4, 3, 5],
      [5, 4, 1]]
Qs = [[2, 1],
      [3, 1],
      [3, 5],
      [1, 2],
      [4, 2]]
rtn1 = func(5, Ws, Qs)
print(rtn1)


