# Definition for singly-linked list.
# class ListNode(object):               #链表的定义
#     def __init__(self, x):
#         self.val = x
#         self.next = None
                                        #总结：已有链表需要提取将l指向l.next后移。
                                        #创建链表需要l.next指向新创建的l。
class Solution(object):
    def addTwoNumbers(self, l1, l2):        #从高位相加，进位保留下来
        carry = 0   ;                        #设置进位标志
        l3 = ListNode(0);
        l4 = l3;                               #创建l4存储最后结果
        l5 = l4;                                #15指向14头，用来返回结果
        while l1 or l2 or carry:

            if l1:
                carry += l1.val;
                l1 = l1.next;
            if l2:
                carry += l2.val;
                l2 = l2.next;
            carry , val = divmod(carry,10);         #求余，carry进位，val当前值

            l3 = ListNode(val);         #create a new listnode
            l4.next  = l3;              #l4.next 指向 新创建的l3节点保存最后数据
            l4 = l4.next ;              #14指向14.next 创建新节点循环
        return l5.next;
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        addends = l1, l2
        dummy = end = ListNode(0)
        carry = 0
        while addends or carry:
            carry += sum(a.val for a in addends)
            addends = [a.next for a in addends if a.next]
            end.next = end = ListNode(carry % 10)
            carry /= 10
        return dummy.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 != None:
            return l2
        elif l1 != None and l2 == None:
            return l1
        elif l1 == None and l2 == None:
            return None
        head = ListNode(0)
        p1 = l1
        p2 = l2
        res = head
        flag = 0
        while(p1 and p2):
            sum_ = p1.val + p2.val + flag
            if sum_ >= 10:
                flag = 1
            else:
                flag = 0
            sum_ %= 10
            res.next = ListNode(sum_)
            p1, p2 = p1.next, p2.next
            res = res.next
        if p2:
            p1 = p2
        while(p1):
            sum_ = p1.val + flag
            if sum_ >= 10:
                flag = 1
            else:
                flag = 0
            sum_ %= 10
            res.next = ListNode(sum_)
            p1 = p1.next
            res = res.next
        if flag == 1:
            res.next = ListNode(1)
        return head.next
            
        

         """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
