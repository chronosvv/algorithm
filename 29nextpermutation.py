# 题意为：
#
# 比如给你个列表是[1,2,3,4]，它的值就是1234，你要找到这四个数字能排出来的刚刚大于1234的数，也就是1243。
# 如果给的是4321，没有比它更大的，就返回最小的也就是1234
#
# Implement next permutation, which rearranges numbers into the lexicographically next
# greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order
# (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs
# are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
#
# 1,1,5 → 1,5,1

class Solution(object):
    def nextPermutation(self, nums):
        """
        :param nums:list[int]
        :return: void do not return anything,modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return

        last = len(nums) - 1
        second_last = last - 1
        while second_last >= 0:
            if nums[second_last] >= nums[second_last+1]:#发现比后面的值大,继续往前比较
                second_last -= 1
            else:#比后面值小
                while last>second_last:
                    if nums[last]>nums[second_last]:#发现第一个比second_last值还大的索引
                        break
                    else:
                        last -= 1
                nums[second_last], nums[last] = nums[last], nums[second_last]#1.值交换
                nums[second_last+1:] = reversed(nums[second_last+1:])#2.倒排
                break #3.完成,跳出
        if second_last == -1: #原排序为从大到小排序
            nums.reverse()

s = Solution()
nums = [1, 2, 3]
s.nextPermutation(nums)
print(nums)