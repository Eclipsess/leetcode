class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return
        p = q = head
        r = None
        i = 0
        while q != None:
            if i != n:
                i +=1
                q = q.next
                continue
            else:
                r = p
                p = p.next
                q = q.next
        if r ==None:
            return head.next
        r.next = p.next
        return head

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class ListNode(object):
    def __init__(self):
        self.head = None
    def __len__(self):
        pre = self.head
        length = 0
        while pre:
            length += 1
            pre = pre.next
        return length
    def add(self, n):
        node = Node(n)

        if self.head == None:
            self.head = node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = node

a = ListNode()
a.add(1)
a.add(2)
a.add(3)
print a.__len__()
b = Solution()
res = b.removeNthFromEnd(a.head,2)
print res.val,res.next.val,

