# 先将短的list合并，再将合并后的list合并，减少比较次数。

# 读题：
# Merge k sorted linked lists and return it
# as one sorted list. Analyze and describe its complexity.

#definition for singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def twoList(self, l1, l2):
        rtn = ListNode(0)
        head = rtn
        while l1 != None or l1!= None:
            if l1!=None and l2!=None:
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

    def merge2List(self, lis):#递归函数调用
        if not lis:
            return None

        if len(lis) < 2:
            return lis[0]

        if len(lis) == 2:#递归终止条件
            return self.twoList(lis[0], lis[1])
        else: #每次将lists均分成两组,分别作merge,再合并
            return self.twoList(self.merge2List(lis[:len(lis)/2]), self.merge2List(lis[len(lis)/2:]))


    def mergeKlists(self, lists):
        """
        :param lists:list[ListNode]
        :return: ListNode
        """
        return self.merge2List(lists)

