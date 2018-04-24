# Given nums = [3,2,2,3], val = 3,
#
# Your function should return length = 2, with the first two elements of nums being 2.

class Solution(object):
    def removeelement(self, nums, val):
        """
        :param nums:list[int]
        :param val: int
        :return: int
        """
        length = len(nums)
        for i in range(length-1, -1, -1):
            if nums[i] == val:
                del nums[i]

        print(nums)

        return len(nums)

s = Solution()
nums = [2, 3, 7, 4, 1, 3]
s = s.removeelement(nums, 3)
print(s)