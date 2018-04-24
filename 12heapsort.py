# 首先堆为一个完全二叉树，因此i父节点的左子节点为2*i+1,右子节点为2*i+2,i的父节点为floor((i-1)/2)，
# 知道这个特性有利于计算。
#
# 堆排序分为两步：
#
# 1.构建大顶堆（既所有父节点都大于他的子节点），虽然不保证堆整体有序，但是顶点一定是所有数中最大的
#
# 2.for倒序循环数组，每次将定点和最后一个子节点交换（交换后子节点为有序数组），重新构建剩下的无序数据，
# 然后重复上述操作。
#
# 复杂度好坏都是nlog(n)

def max_root(data, root, size):
    #get max root heap
    while root<=(size-2)/2:
        left = root*2 + 1
        right = root*2 + 2
        larger = root
        if left < size and data[left] > data[larger]:
            larger = left
        if right < size and data[right] > data[larger]:
            larger = right
        if larger != root:
            change = data[larger]
            data[larger] = data[root]
            data[root] = change
            root = larger
        else:
            root = size

def get_heap(data):
    #change ordinary data to heap
    for i in range((len(data)-2)//2, -1, -1):
        max_root(data, i, len(data))

def get_sorted_heap(data):
    #heap sort
    #1.change data to heap
    get_heap(data)
    #2.sort heap data
    for i in range(len(data)-1, -1, -1):
        change = data[i]
        data[i] = data[0]
        data[0] = change
        max_root(data,0,i)

if __name__ == "__main__":
    data = [2,4,5,1,8,12,6,5,7]
    get_sorted_heap(data)
    print(data)