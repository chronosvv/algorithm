# 本体的思路集中在理解题意和栈的关系，每当看到一个左括号，就压栈一个右括号，
# 当遇到一个右括号，看一下此右括号是否和栈顶字符相同，相同则继续，否则一定是违规的。
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid
# but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        """
        :param s:str
        :return: bool
        """
        dic = {"(":")", "{":"}", "[":"]"}
        lis = []
        length = len(s)
        for i in range(length):
            if s[i] in dic: #若是左括号,dic的key
                lis += [dic[s[i]]] #lis存储的是右括号
                # print(s[i])
            else: #若是右括号,则需要跟list尾字符一致
                if len(lis) < 1:#没有左括号
                    return False
                last = lis[-1]
                if last != s[i]:
                    return False
                else:
                    del lis[-1]

        if len(lis) == 0:#最后还要判断是否lis为空,即所有左括号都找到了右括号
            return True
        else:
            return False

# s = Solution()
# strs = "{[]}"
# s = s.isValid(strs)
# print(s)

# dic = {"(":")", "{":"}", "[":"]"}
# if "[" in dic:
#     print("True")
# else:
#     print("False")