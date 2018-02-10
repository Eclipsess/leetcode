# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        size = len(lists)
        mid = size/2
        if size == 0:
            return None
        if size == 1:
            return lists[0]
        
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        head = cur = ListNode(0)
        
        while left or right:
            if right == None or (left and left.val <= right.val):
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        return head.next
            