# 本题为Z型字符重排，重点是考虑好转折点的边界条件，同时排除一些异常情况，难度不大。

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
# like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution(object):
    def convert(self, s, numRows):
        """
        :param s:str
        :param numRows:int
        :return: str
        """
        if not numRows or numRows == 1 or len(s) <= numRows:
            return s

        dic = {}
        count = 0 #count表示第几行
        reverse = False #False表示从上往下,True表示从下往上
        for i in range(len(s)):
            if count < numRows and not reverse:
                if count in dic:
                    dic[count] += s[i]
                else:
                    dic[count] = s[i]
                count += 1
                if count == numRows:
                    reverse = True
            else:
                if count == numRows:
                    count -= 2 # (倒数第二个位置,从下往上数)
                else:
                    count -= 1
                dic[count] += s[i]
                if count == 0:
                    count += 1
                    reverse = False
        rtn = ""
        for i in range(numRows):
            rtn += dic[i]
        return rtn