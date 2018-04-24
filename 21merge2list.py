# 本题思想为递归排序，原理是从两个数组中取出head进行比较，把小的放到目标数组中。
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :param l1:ListNode
        :param l2: ListNode
        :return: ListNode
        """

        rtn = ListNode(0)
        head = rtn
        while (l1!=None) or (l2!=None):#如果l1和l2都为空,停止循环
            if l1!= None and l2!=None:
                if l1.val < l2.val:
                    rtn.next = l1
                    rtn = rtn.next
                    l1 = l1.next
                else:
                    rtn.next = l2
                    rtn = rtn.next
                    l2 = l2.next

            elif l1 != None:
                rtn.next = l1
                break

            else:
                rtn.next = l2
                break

        return head.next
