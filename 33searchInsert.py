# 本道为easy，考察二分查找
#
# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.

# Input: [1,3,5,6], 5
# Output: 2
#
# Input: [1,3,5,6], 2
# Output: 1
#
# Input: [1,3,5,6], 7
# Output: 4
#
# Input: [1,3,5,6], 0
# Output: 0

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :param nums:List[int]
        :param target: int
        :return: int
        """
        start = 0
        end = len(nums) - 1
        mid  = (start + end) // 2
        while start < end:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid + 1
            mid = (start + end) // 2

        if nums[mid] < target:
            return mid + 1
        else:
            return mid

s = Solution()
s = s.searchInsert([1, 3, 5, 6], 2)
print(s)