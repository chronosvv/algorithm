# 本题与15题思路一样，本质都是找与target更近的地方，
# 先对数组排序，然后在每个循环里设置两个指针从两边向中间遍历，代码如下。
#
# Given an array S of n integers, find three integers in S such that
# the sum is closest to a given number, target. Return the sum of the three integers.
# You may assume that each input would have exactly one solution

# For example, given array S = {-1 2 1 -4}, and target = 1.
#
# The sum that is closest to the target is 2.(-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :param nums:list[int]
        :param target: int
        :return: int
        """
        arr = sorted(nums)
        length = len(arr)
        final_sum = arr[0] + arr[1] + arr[2]
        final_gap = abs(final_sum - target)
        for i in range(length):
            start = i + 1
            end = length - 1
            while start < end:
                value = arr[start] + arr[i] + arr[end]
                this_gap = abs(value - target)

                if final_gap > this_gap:
                    final_sum = value
                    final_gap = this_gap
                if target > value:
                    start += 1
                else:
                    end -= 1
        return final_sum

# a = ("2, 3, 4").split(",")
# for i in a:
#     print(i)