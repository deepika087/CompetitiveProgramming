__author__ = 'deepika'

"""

27 / 27 test cases passed.
Status: Accepted
Runtime: 56 ms
"""
def printList(listNodes):
    temp = listNodes
    while(temp):
        print " %d " %(temp.val),
        temp = temp.next

def getList(arr):
    start, temp = None, None
    for _a in arr:
        if start is None:
            start = ListNode(_a)
            temp = start
        else:
            temp.next = ListNode(_a)
            temp = temp.next
    return start


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            print "Returning: ", prev
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)

    def reverseListIterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        q, r, s = head, None, None
        while q:
            s = q.next
            q.next = r
            r = q
            q = s
        return r

print "Before"
q = getList([1, 2, 3, 4])
#q = getList([1])
printList(q)
s = Solution()
r = s.reverseList(q)
print "After"
printList(r)


