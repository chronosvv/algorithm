'''一般而言,对于包含n个元素的列表,用二分查
找最多需要log 2 n步,而简单查找最多需要n步'''

def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high)
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None

# def binary_search(lst, item):
#     low = 0
#     high = len(lst) - 1
#     while low <= high:
#         mid = int((low + high) / 2)
#         guess = lst[mid]
#         if guess == item:
#             return mid
#         elif guess < item:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return None
#
# mylist = [1, 2, 3, 4, 5, 6]
#
# print(binary_search(mylist, 3))

#练习：
# 1.1假设有一个包含128个名字的有序列表,你要使用二分查找在其中查找一个名字,请问最多需要几步才能找到?
# 1.2 上面列表的长度翻倍后,最多需要几步?


'''假设列表包含n个元素。简单查找需要检查每个元素,因此需要执行n次 操作。使用大O表示法,
这个运行时间为O(n)。 大O表示法让你能够 比较操作数,它指出了算法 运行时间的增速'''

# 一些常见的大 O 运行时间
#  O(log n),也叫对数时间,这样的算法包括二分查找。
#  O(n),也叫线性时间,这样的算法包括简单查找。
#  O(n * log n),这样的算法包括第4章将介绍的快速排序——一种速度较快的排序算法。
#  O(n 2 ),这样的算法包括第2章将介绍的选择排序——一种速度较慢的排序算法。
#  O(n!),这样的算法包括接下来将介绍的旅行商问题的解决方案——一种非常慢的算法。

#  算法的速度指的并非时间,而是操作数的增速。
#  谈论算法的速度时,我们说的是随着输入的增加,其运行时间将以什么样的速度增加。
#  算法的运行时间用大O表示法表示。
#  O(log n)比O(n)快,当需要搜索的元素越多时,前者比后者快得越多。

# 练习
# 使用大O表示法给出下述各种情形的运行时间。
# 1.3 在电话簿中根据名字查找电话号码。
# 1.4 在电话簿中根据电话号码找人。(提示:你必须查找整个电话簿。)
# 1.5 阅读电话簿中每个人的电话号码。
# 1.6 阅读电话簿中姓名以A打头的人的电话号码。这个问题比较棘手,它涉及第4章的概念。答案可能让你感到惊讶!

def er(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = lst[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1

    return None

mylst = [7, 13, 35, 56, 27, 33, 92]
print(er(mylst, 315))