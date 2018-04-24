# 本题可以套用3sum,在最外层多套用一层循环，详见代码
#
# Given an array S of n integers, are there elements a, b, c, and d in S
# such that a + b + c + d = target? Find all unique quadruplets in the array
# which gives the sum of target.
#
# Note: The solution set must not contain duplicate quadruplets.
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    def __init__(self):
        self.unique = []

    def threeSum(self, nums, target, v):#原理和3sum一样
        length = len(nums)
        if length < 3:
            return None
        for i in range(length):
            start = i + 1
            end = length - 1
            while start < end:
                value = nums[i] + nums[start] + nums[end]
                if value == target and [v,nums[i], nums[start], nums[end]] not in self.unique:
                    self.unique += [[v, nums[i], nums[start], nums[end]]]
                    start += 1
                    end -= 1
                elif value < target:
                    start += 1
                else:
                    end -= 1
        # print(self.unique)

    def fourSum(self, nums, target):
        """
        :param nums:List[int]
        :param target: int
        :return: List[List[int]]
        """
        arr = sorted(nums)
        length = len(arr)
        for i in range(length):#4sum多一层循环
            self.threeSum(arr[i + 1:], target - arr[i], arr[i])

        return self.unique

s = Solution()
nums = [1, 0, -1, 0, -2, 2]
s = s.fourSum(nums, 0)
print(s)