# 基本思想是，若p的第二个不是*，那么第一个字符必须相等（或p的一个为'.'），然后p和s各加一位继续递归比较
# 若p的第二个是*，那么第一个字符必须和s的前n个相等，n可以while循环找到最后一个，然后再递归

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aaaab", "c*a*b") → true

class Solution(object):
    def isMatch(self, s, p):
        """
        :param s:str
        :param p: str
        :return: bool
        """
        sLen = len(s)
        pLen = len(p)
        if(pLen == 0):
            return sLen == 0
        if(pLen == 1):
            if (p == s) or ((p == '.') and (len(s) == 1)):
                # print('aaaa')
                return True
            else:
                # print('bbbb')
                return False

        #p的最后一个字符不是'*'也不是'.'且不出现在s里,p跟s肯定不匹配
        if(p[-1] != '*') and (p[-1] != '.') and (p[-1] not in s):
            # print('dnw')
            return False
        if(p[1] != '*'):
            if(len(s) > 0) and ((p[0] == s[0]) or (p[0] == '.')):
                return self.isMatch(s[1:], p[1:])
            # print('hhh')
            return False
        else:
            while (len(s) > 0) and ((p[0] == s[0]) or (p[0] == '.')):
                if(self.isMatch(s, p[2:])):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])

c = Solution()
a = c.isMatch(".*", "ab")
print(a)