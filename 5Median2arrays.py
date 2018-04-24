# 本题难度为hard，要考虑全数组边界情况，可以转换为求两个有序数组第K个值。

# 基本思想是，在排除一些边界条件后，两个数组分别通过二分查找（二分时间复杂度是log(m+n)），
# 通过二分后数据的数量和K的大小来进行下一轮二分两个数组的起始、结束点与新K值的确定。

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).

# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0

# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        # print("l:{}".format(l))
        if l % 2 == 1:
            return self.kth(A, B, l//2) #中位数
        else:
            return (self.kth(A, B, l//2) + self.kth(A, B, l//2 - 1)) / 2.0 #中位数的平均值

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]

        ia, ib = len(a) // 2, len(b) // 2
        # print(ib)
        ma, mb = a[ia], b[ib]
        # print("ma:{},mb:{}".format(ma, mb))

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # print("<")
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia -1)
        # when k is smaller than the sum of a and b's median indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

nums1 = [1, 2]
nums2 = [3, 4]
m = Solution()
a = m.findMedianSortedArrays(nums1, nums2)
print(a)
# print(8 / 5)