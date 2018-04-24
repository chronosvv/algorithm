#1.判断链表是否有环：

# 网搜思路：定义两个变量，一个每次走一步，另一个每次走两步，若链表有环，则他们最后必将在环内无止境循环，
# 快的一定会给慢的套圈，因此他俩一定
# 会在某处遇到，这是这个问题的前提，了解这个就知道接下来解题思路了

class Solution(object):
    def hasCycle(self, head):
        '''
        :param head: ListNode
        :return: bool
        '''
        if head == None:
            return False

        #定义两个变量：first：一次走一步 second：一次走两步
        first = head.next
        if first == None:
            return False

        second = first.next
        while second != None: #second走到null循环结束
            if first == second:
                return True #second和first为同一值，说明两个变量有重合（first被second套圈，若不终止则会一直循环）
            first = first.next
            second = second.next
            if second == None:
                return False
            second = second.next
        return False #最后没有找到圈返回False

#2.引申问题，判断链表环的入口
#网搜思路：还是定义两个变量，一个一次一步，另一个一次两步，那么他们在环内相遇的时候，慢的走了s步，快的走了2s步
#假设环的入口距离head有x步，他们在环内相遇时慢的在环内走了y步，环本身有N步，则有下式
#慢：s = x + y (慢的在相遇前一定没走慢一圈，这里可以用假设法)
#快：2s = x + y + nN(快的在与慢的相遇前自己可能在环内走了n圈，n>=0)

#x = nN-y ///x = N-y +(n-1)N 如果一个从相遇点开始走，另一个从head开始走，一次均一步，则他们第一次相遇的位置就是环的入口

class Solution2(object):
    def detectCycle(self, head):
        """
        :type head:ListNode
        :rtype:ListNode
        """
        #1.先找出快慢相遇点位置
        if head == None:
            return None

        #定义两个变量，first：一次走一步 second：一次走两步
        first = head.next
        if first == None:
            return None
        second = first.next
        Flag = False
        while second != None:#second走到null循环结束
            if first == second:
                Flag = True
                break#second和first指向同一值，说明两个变量有重合
            first = first.next
            second = second.next
            if second == None:
                return None
            second = second.next
        if not Flag:#没找到环
            return None
        #third从head开始走，first继续走，他两第一次相遇的位置就是入口
        third = head
        while third != first:
            third = third.next #另一个从head开始走
            first = first.next #如果一个从相遇点开始走
        return third
