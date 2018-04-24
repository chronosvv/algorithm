# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator.
# Return the quotient after dividing dividend by divisor.
#
# Input: dividend = 10, divisor = 3
# Output: 3
#
# Input: dividend = 7, divisor = -3
# Output: -2


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :param dividend:int
        :param divisor: int
        :return: int
        """
        if dividend == 0 or divisor == 0:
            return 0
        n = 0
        POW = 0
        neg = False
        if (dividend > 0) is (divisor < 0):
            neg = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend > (divisor * (10**POW)):
            POW += 1
        while POW >= 0:
            if dividend >= divisor * (10 ** POW):
                dividend -= divisor * (10 ** POW)
                n += 10**POW
            else:
                POW -= 1
        if neg:
            n = -n
        return min(n, 2147483647)

s = Solution()
s = s.divide(3, 2)
print(s)