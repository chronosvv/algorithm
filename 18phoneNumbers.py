# 本题不是特别难，从后往前套两层for循环基本就出来了。不用递归看起来舒适些
#
# Given a digit string, return all possible letter combinations that the number could
# represent. A mapping of digit to letters (just like on the telephone buttons) is
# given below.

# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution(object):
    def letterCombinations(self, digits):
        """
        :param digits:str
        :return: List[str]
        """
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno",
               "7":"pqrs", "8":"tuv", "9":"wxyz"}
        index = len(digits) - 1
        if index < 0:
            return []
        rtn = [""]

        while index > -1:
            rtn = [b+a for a in rtn for b in dic[digits[index]]]
            index -= 1
        return rtn

s = Solution()
digits = "23"
s = s.letterCombinations(digits)
print(s)


# rtn = [b+a for a in ['d','e','f'] for b in ['a','b','c']]
# print(rtn)
