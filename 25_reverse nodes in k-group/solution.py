# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        if k <= 1:
            return head
        head0 = ListNode(0)
        head0.next = head
        node = head0
        while node:
            node = self.reverseKnode(node, k)
        return head0.next
    
    def reverseKnode(self, node, k):
        judge = node
        for i in range(k):               # if use while(k > 0): k -= 1 .when next time use k , k  = 0 not k = k
            if not judge.next:
                return None
            judge = judge.next
            
        cur = node.next
        pre = node
        node1 = node.next
        for i in range(k):                 # k was changed, so Time limit exceed
            after = cur.next
            cur.next = pre
            pre = cur
            cur = after
        node.next = pre
        node1.next = cur
        return node1