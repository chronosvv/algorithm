# 本题之前一直纠结如何循环调用，后来看网上思路有人用到递归，整理后的代码如下，
#
# 基本思路是：
#
# 1.左边括号数要大于右边括号数
#
# 2.在1的原则下，每次递归为字符串赋值"("或")"
#
# 3.每次递归生成两个分支，分别往下去找，最终找到所有组合
#
# Given n pairs of parentheses, write a function to generate all combinations of
# well-formed parentheses.
#
# For example, given n = 3, a solution set is:
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution(object):
    def func(self, array, string, left, right):
        """
        :param array: 最终生成的list
        :param string: 本轮已经完成的str
        :param left: 左括号剩余个数
        :param rigt: 右括号剩余个数
        """
        if left == 0 and right == 0:#递归终止条件,左括号和右括号的剩余个数均为0
            array += [string]
        if left > 0:#左括号剩余大于0,继续往下递归
            self.func(array, string+"(", left-1, right)
        if right > 0 and left < right:#右括号剩余个数大于0,且左边小于右边,继续递归
            self.func(array, string+")", left, right-1)

    def generateParenthese(self, n):
        """
        :param n:int
        :return: List[str]
        """
        rtn = []
        self.func(rtn, "", n, n)
        return rtn

s = Solution()
s = s.generateParenthese(2)
print(s)
