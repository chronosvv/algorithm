# 给定n个非负整数a1,a2,...,an,其中每个代表一个点坐标(i, ai).n个垂直线段例如线段的
# 两个端点在(i, ai)和(i,0).找到两个线段,与x轴形成一个容器,使其包含最多的水.

# 重点是从两边开始比较，遇到边比两边还短的直接跳过。

class Solution(object):
    def maxArea(self, height):
        """
        :param height: List[int]
        :return: int
        """
        right = len(height) - 1
        left = 0
        max_col = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            col = w * h
            max_col = max(col, max_col)

            #遇到边短的直接跳过
            while height[left] <= h and left < right:left+=1
            while height[right] <= h and right > left:right-=1

        return max_col
