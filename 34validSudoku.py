# 本题判断数独题，难度medium，行和列单独设置一个字典好判断，九宫格号如何计算 是本题难点。
#
# 根据数字下标我们发现，行号/3 * 10 + 列号/3*100可以把九宫格 区分开来，然后再判断九宫格里有无此数字即可，
# 详见代码。
#
# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated
# according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true

# Input:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being
#     modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :param board:list[list[str]]
        :return: bool
        """
        row_dic = {}
        col_dic = {}
        dic = {}
        #十位:行 十位:列 十位,百位:九宫格号,先数行后数列
        for i in range(len(board)):#行循环
            for j in range(len(board[i])):#列循环
                if board[i][j] == ".":
                    continue
                #1.判断行
                val = i*10 + int(board[i][j])
                if val in row_dic:
                    return False
                else:
                    row_dic[val] = 1
                #2.判断列
                val = j*10 + int(board[i][j])
                if val in col_dic:
                    return False
                else:
                    col_dic[val] = 1
                #判断九宫格号
                val = (i//3) * 10 + (j//3) * 100 + int(board[i][j])
                if val in dic:
                    return False
                else:
                    dic[val] = 1

        return True

s = Solution()

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

s = s.isValidSudoku(board)
print(s)