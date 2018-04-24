# 题目：
#
# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# 思路：用到了python的find函数，找到字符出现在 子串的位置，
# 然后下一个起始点为本轮起始点+字串出现重复的位置的下一个

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :param s:str
        :return: int
        """
        if not s:
            return 0

        max_sub = "" #存放最大字符串
        find_sub = "" #存放出现的字符串

        end = 0
        begin = 0

        while end < len(s):
            if find_sub.find(s[end]) < 0:#find_sub字符串里面不包含s[end]
                find_sub += s[end]
                if end - begin + 1 > len(max_sub):
                    max_sub = s[begin:end+1]

            else:
                sub_begin = find_sub.find(s[end])

                begin += sub_begin+1 #重复字符的下一个开始
                find_sub = s[begin:end+1]

            end += 1
        print(max_sub)

        return len(max_sub)

s = Solution()
lens = s.lengthOfLongestSubstring("acjajdssi")
print(lens)
