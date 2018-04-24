# 循环递增数组有一个性质：以数组中间元素将循环递增数组划分为两部分，则一部分为一个严格递增数组，
# 而另一部分为一个更小的循环递增数组。本题的思路每次二分查找，判断target在一侧有序的数组还是在无序的数组里，
# 在判断有序数组里一定要记着比较数组最大和最小值。

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you
# beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index,
# otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).

# Input: nums = [
# 4,5,6,7,0,1,2]
# , target = 0
# Output: 4
#
# Input: nums = [
# 4,5,6,7,0,1,2]
# , target = 3
# Output: -1
class Solution(object):
    def search(self, nums, target):
        """
        :param nums: list[int]
        :param target: int
        :return: int
        """
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start+end) // 2
            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid]: #mid左侧正序
                if target < nums[mid] and target >= nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            else: #右侧正序
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

s = Solution()
s = s.search([4, 5, 6, 7,0, 1, 2], 0)
print(s)