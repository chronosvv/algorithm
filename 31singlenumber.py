# 本题的思路是寻找一组数种出现一次的两个数，此题有如下特点：
#
# 1.数异或自己等于0
#
# 2.两个不一样的数异或不为0
#
# 具体思路看代码
#
# Given an array of numbers nums, in which exactly two elements appear only once and
# all the other elements appear exactly twice. Find the two elements that appear only once.
#
# For example:
#
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
#
# Note:
#
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only
# constant space complexity?

# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all
#  test cases.
class Solution(object):
    def singleNumber(self, nums):
        """
        :param nums:list[int]
        :return: list[int]
        """
        # 1.将所有数异或,找到不为0的值xor
        xor = 0
        for num in nums:
            xor ^= num
        # 2.找到第一个不为1的那一位对应的数flag
        flag = (xor& (xor-1)) ^xor #括号里将第一个为1的位置零,再异或就找到了
        # 3.将数据分别与flag相与,为0的一组
        rtn1 = 0
        rtn2 = 0
        for num in nums:
            if num & flag != 0:
                rtn1 ^= num
            else:
                rtn2 ^= num
        return [rtn1, rtn2]

s = Solution()
s = s.singleNumber([1, 2, 1, 3, 2, 5])
print(s)