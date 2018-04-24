# 本题开始想到的是暴力搜索的方式，首先编写判断一个字符串是否是回文（这个相对容易），
# 然后再写两个循环遍历字符串所有子串，但是这种方法超时了。
#
# 网搜有很多种解决方案，如动态规划、中心扩展法，本文介绍的是后者。
# 中心扩展法核心思想是：分开考虑奇数和偶数情况，然后从中心向两边扩展，找到最大的长度，
# 记录起始位置与中心半径长度，根据半径找到最大回文子串。
#
# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.

# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.

# Input: "cbbd"
#
# Output: "bb"

class Solution(object):
    def __init__(self):
        self.low = 0
        self.R = 0

    def logestPalindrome(self, s):
        """
        :param s:str
        :return: str
        """
        # 1.如果s为空或只有一个字符，则返回s本身
        if s == None or len(s) == 1:
            return s

        # 2.从子串中心向两边扩展
        for i in range(len(s)):
            # 分两步做
            # 1.考虑奇数aba这种情况
            self.judge(s, i, i)
            # 2.考虑偶数abba这种情况
            self.judge(s, i, i+1)
        return s[self.low:self.low + self.R]

    def judge(self, string, start, end):
        #从start/end开始向string的两边扩展，寻找对称点
        while 0<=start and end<len(string) and string[start] == string[end]:
            if end - start + 1 > self.R:
                self.R = end - start + 1
                self.low = start
            start -= 1
            end += 1
