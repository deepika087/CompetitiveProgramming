"""
207 / 207 test cases passed.
Status: Accepted
Runtime: 52 ms
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if (n ==1 and head.next == None):
            return None
        save=head
        prev=None
        start = head
        while(head and n > 0):
            head = head.next
            n = n - 1
        while(head is not None):
            head=head.next
            prev=start
            start=start.next
        if (prev is None):
            save=save.next
        else:
            prev.next = start.next
        #print "prev now points to : ", prev.next.val if prev.next is not None else "Null"
        return save



head=ListNode(1)
#head.next=ListNode(2)
#head.next.next=ListNode(3)
#head.next.next.next=ListNode(4)
#head.next.next.next.next=ListNode(5)
#head.next.next.next.next.next=ListNode(6)

s=Solution()
s.removeNthFromEnd(head, n=1)
