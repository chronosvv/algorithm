# 本题和2sum类似，区别是固定一点不动，然后就可套用2sum的代码了，只是本题要求不能有重复组合，
# 因此需要一个hash记录一下已经使用的组合。

# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def threeSum(self, nums):
        """
        :param nums:list[int]
        :return: list[list[int]]
        """
        arr = sorted(nums)
        length = len(arr)
        hash_data = {}
        rtn = []
        last = None
        for i in range(length-2):
            if last == arr[i]:
                continue
            last = arr[i]
            start = i + 1
            end = length - 1
            value = arr[i]
            while start < end:
                total = arr[start] + arr[end] + value
                if total == 0:
                    key = str(arr[start]) + ":" + str(arr[end])
                    if key not in hash_data:
                        rtn += [[value, arr[start], arr[end]]]
                        hash_data[key] = 0
                    else:
                        end -= 1
                        start += 1
                elif total > 0:
                    end -= 1
                else:
                    start += 1

        return rtn

s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
s = s.threeSum(nums)
print(s)