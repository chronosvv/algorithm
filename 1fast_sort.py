# 快速基本思想是：通过一趟排序将要排序的数据分割成独立的 两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
# 然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
# 考点：
# 1.时间复杂度：平均时间复杂度是O(n*logn)，最快是O(n*logn),最差(每一次取到的元素就是数组中最小/最大的)O(n2)
# 2.空间复杂度：最优O(log(n)),最差O（n）

# 快速排序，升序
import random
def fast_search(array, start, end):
    if not array:
        return
    if len(array) == 0:
        return
    if start >= end:
        return

    # 保存start和end的值 供递归
    store_start = start
    store_end = end

    # 随机取一个索引，比取固定位置平均复杂度低
    index = random.randint(start, end)
    value = array[index]

    # 将第一个元素与 随机值互换，为了方便使用 第一个元素的位置，且随机值就是value，可以被覆盖。
    # 最后value赋值给start。
    store = array[start]
    array[start] = array[index]
    array[index] = store

    while start < end:
        while(start < end) and (array[end] >= value):
            end -= 1
        while(start < end) and (array[end] < value):
            array[start] = array[end] #小的放前面
            start += 1
            array[end] = array[start] #把前面的元素送给end位置与value比较
    array[start] = value
    fast_search(array, store_start, end)
    fast_search(array, end+1, store_end)

if __name__ == "__main__":
    array = [1, 100, 50, 99, 48, 22, 77]
    fast_search(array, 0, len(array)-1)
    print(array)