# 本题主要思路是定义快慢指针，各每次走两步，再进行值交换。注意题目要求不能改值，代码如下
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. You may not modify the values in the list,
# only nodes itself can be changed.

#definition for singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :param head:ListNode
        :return: ListNode
        """
        if not head:
            return head
        slow = head
        fast = head.next
        last_one = None #两两交换 上一个指针,用于保证链表不断

        while fast != None:
            fast.next, slow.next = slow, fast.next
            if last_one: #非首部
                last_one.next = fast
            else:#首部重新定义
                head = fast
            last_one = slow
            slow = slow.next
            if slow:
                fast = slow.next
            else:
                break
        return head