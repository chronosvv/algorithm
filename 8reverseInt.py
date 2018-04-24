# 本题要考虑边界条件32bit有符号int最大值为2^31-1,最小为-2^31，整数反转思想如下代码

# Given a 32-bit signed integer, reverse digits of an integer.

# Input: 123
# Output:  321
#
# Input: -123
# Output: -321

# Input: 120
# Output: 21

# Assume we are dealing with an environment which could only hold
#  integers within the 32-bit signed integer range. For the purpose
#  of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :param x:int
        :return: int
        """
        y = 0
        flag = True
        if x < 0:
            flag = False
            x = abs(x)
        max_v = 2**31 - 1
        max_neg_v = 2 ** 31
        while x != 0:
            y = y * 10 + x % 10
            x = int(x / 10)
            if flag and y > max_v:
                return 0
            elif not flag and y > max_neg_v:
                return 0

        if flag:
            return y
        else:
            return -y

s = Solution()
r = s.reverse(1232)
print(r)