# 动态规划实际上是一个局部贪心问题，在考虑是否把一个物品加入背包前，考虑：

# max（背包已有物品总价值，max（背包已有物品-此物品重量的物品总价值）+此物品总价值）。

# 题目： 有编号分别为a,b,c,d,e的五件物品，它们的重量分别是2,2,6,5,4，它们的价值分别是6,3,5,4,6，
# 每件物品数量只有一个，现在给你个承重为10的背包，如何让背包里装入的物品具有最大的价值总和？
# 背包问题分为两步：
#  1)正向遍历item,每个item遍历不同包重量，考虑不同包重量下，加（不加）此item所获取的最大价值
#  2)给定包重量，反向遍历item（反向是因为最后的item是看到之前所有item得到的最优解）,比较item与item-1谁更优，
# 然后再接着遍历下一个item
#
# 重点：
#
# 理解矩阵d[i][j]的含义：前i个物品放入重量为j的背包里所能获取的最大收益，正因为背包问题可以有这样的递推公式，
# 因此可以从局部最优推导到全局最优

def packbag(weight, value, totalValue):
    #初始化数组,横纵多出一个维度方便计算
    weight_value = [[0 for i in range(totalValue+1)] for j in range(len(weight)+1)]
    # print(weight_value)
    weight = [0] + weight
    value = [0] + value
    #第一步,构建二维数组
    for item in range(1, 5+1):
        for total_weight in range(1, 10+1):
            #first init this item value with last item value
            weight_value[item][total_weight] = weight_value[item-1][total_weight]
            #call this item value
            if total_weight-weight[item] < 0:
                this_value = weight_value[item-1][total_weight]
            else:
                this_value = weight_value[item-1][total_weight-weight[item]] + value[item]

            if this_value > weight_value[item][total_weight]:
                weight_value[item][total_weight] = this_value

            print("item:%d,total_weight:%d,%d" % (item, total_weight, weight_value[item][total_weight]))
            # print(this_value)
    #第二步,反向遍历
    choose = []
    for item_num in range(len(weight)-1, 0, -1):
        if weight_value[item_num][totalValue] > weight_value[item_num-1][totalValue]:
            choose.append(item_num)
            totalValue = totalValue-weight[item_num]

    total = 0
    for i in choose:
        total += value[i]

    return total, choose

if __name__ == "__main__":
    weight=[2,2,6,5,4]
    value = [6,3,5,4,6]
    totalValue = 10
    rtn,choose = packbag(weight, value, totalValue)
    print("total value:%d, choose:%s" %(rtn, str(choose)))
    # for i in range(1,3):
    #     print(i)