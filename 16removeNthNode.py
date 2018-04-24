# 删除倒数第N个节点，此类问题需要两个快慢指针，快指针先走N+1步，然后和慢指针一起走，当快指针为None的时候，
# 慢指针的位置为倒数N+1的位置，因此可以通过slow.next=slow.next.next删除第N个节点。
#
# 此问题还要考虑到删除head节点的情况。代码如下
#
# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Note:
# Given n will always be valid.
# Try to do this in one pass.

# Definition for singly-link list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :param head:ListNode
        :param n: int
        :return: ListNode
        """
        fast = head
        slow = head

        m = n + 1
        while fast and m:
            fast = fast.next
            m -= 1 #若最后m为1,则说明遍历到fast到链表尾部了,此次要删除的是head

        while fast:
            fast = fast.next
            slow = slow.next

        if m == 1: #删除的是head的情况
            return head.next
        else:
            slow.next = slow.next.next
            return head
