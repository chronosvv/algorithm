# 本题为给一个有序数组，让你返回无重复元素个数，并且原数组只保留无重复元素，因为要删除数组元素，
# 因此遍历的时候要从后往前遍历，防止原元素顺序紊乱。

# Given a sorted array, remove the duplicates in-place such that each element appear
# only once and return the new length.Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.
#
# Example:
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being
# 1 and 2 respectively.It doesn't matter what you leave beyond the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :param nums:list[int]
        :return: int
        """
        if not nums:
            return 0
        length = len(nums)
        flag = nums[length-1]
        length = length - 1
        count = 1
        while length:#有删除列表元素操作,从后往前遍历,保证列表原有顺序
            if nums[length - 1] != flag:#没有重复count+1
                flag = nums[length - 1]
                count += 1
            else:#若有重复即删除
                del nums[length - 1]

            length -= 1

        return count