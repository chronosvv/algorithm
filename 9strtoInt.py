class Solution(object):
    def myAtoi(self, stri):
        """
        :param stri:str
        :return: int
        """
        if not stri:
            return 0

        while stri[0] == " ":
            if len(stri) == 1:
                return 0
            else:
                stri = stri[1:]

        if len(stri) == 1 and self.judgeNum(stri[0]):
            return int(stri)
        elif len(stri) == 1:
            return 0
        else:
            flag = True
            start = 0
            if stri[0] == '-':
                flag = False
                start = 1
            elif stri[0] == '+':
                start = 1
            elif not self.judgeNum(stri[0]):
                return 0
            rtn = 0
            #正负最大最小值设置
            max_int = 2147483647
            min_int = 2147483648
            first = False
            for i in range(start, len(stri)):
                if self.judgeNum(stri[i]):
                    rtn = rtn * 10 + int(stri[i])
                    first = True
                    if flag and rtn > max_int:
                        return max_int
                    if not flag and rtn > min_int:
                        return -min_int
                else:
                    if first:
                        return self.ret(flag, rtn)
                    else:
                        return 0

            return self.ret(flag, rtn)

    def ret(self, flag, rtn):
        if flag:
            return rtn
        else:
            return -rtn

    def judgeNum(self, char):
        #判断是否是数字
        if '0' <= char <= '9':
            return True
        else:
            return False

c = Solution()
mya = c.myAtoi('127')
print(mya)