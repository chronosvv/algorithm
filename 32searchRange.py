# 本题的解决思路是先找到target的开始位置，然后顺着开始位置找到结束为止，注意找开始位置的用法
#
# Given an array of integers nums sorted in ascending order, find the starting and ending
# position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Input: nums = [
# 5,7,7,8,8,10]
# , target = 8
# Output: [3,4]
#
# Input: nums = [
# 5,7,7,8,8,10]
# , target = 6
# Output: [-1,-1]

class Solution(object):
    def searchRange(self, nums, target):
        """
        :param nums:List[int]
        :param target:int
        :return:list[int]
        """
        if not nums:
            return [-1, -1]
        #第一步 找到target的起始位置end
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        while start < end:
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
            mid = (start + end) // 2

        if nums[end] != target:
            return [-1, -1]
        #第二步 找到target的终止位置
        left = end
        right = end
        while (right < len(nums)) and (nums[right] == target):
            right += 1

        return [left, right-1]

s = Solution()
s = s.searchRange([5,7,7,8,8,10], 8)
print(s)