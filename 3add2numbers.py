# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :param l1:listNode
        :param l2:listNode
        :return:listnode
        """
        #初始化进位
        increment = 0
        #初始化返回值
        rtn = cal = ListNode(0)

        while True:
            total = 0
            if l1 != None and l2 != None:
                total = l1.val + l2.val + increment
                cal.val = total % 10
                increment = total / 10
                l1 = l1.next
                l2 = l2.next
            elif l1 != None:
                total = l1.val + increment
                cal.val = total % 10
                increment = total / 10
                l1 = l1.next
            elif l2 != None:
                total = l2.val + increment
                cal.val = total % 10
                increment = total / 10
                l2 = l2.next
            elif increment != 0:
                cal.val = increment
                break
            else:
                break

            #指向下一位
            if l1 != None or l2 != None or increment:
                cal.next = ListNode(0)
                cal = cal.next
            else:
                break

        return rtn

class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        rtn = cal = ListNode(0)
        increment = 0
        while l1 or l2 or increment:
            a = l1.val if l1 and l1.val else 0
            b = l2.val if l2 and l2.val else 0
            cal.val = (a + b + increment) % 10
            increment = (a + b + increment) / 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 or l2 or increment:
                cal.next = ListNode(0)
                cal = cal.next

        return rtn

