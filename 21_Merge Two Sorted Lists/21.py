# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        if l1.val < l2.val:
            head, r = l1, l1
            l1 = l1.next
        else:
            head, r = l2, l2
            l2 = l2.next
        
        while(l1 and l2):
            if l1.val < l2.val:
                r.next = l1
                l1 = l1.next
            else:
                r.next = l2
                l2 = l2.next
            r = r.next
        if l1 == None:
            r.next = l2   # not r = l2
        else:
            r.next = l1
            
        return head    # not r