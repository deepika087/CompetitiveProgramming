__author__ = 'deepika'

"""
44 / 44 test cases passed.
Status: Accepted
Runtime: 35 ms
Beats: 70%
"""

def printList(listNodes):
    result = []
    temp = listNodes
    while(temp):
        result.append(temp.val)
        temp = temp.next
    return result

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
    def reverse(self, start):
        q, r, s = start, None, None
        while q:
            s = q.next
            q.next = r
            r = q
            q = s
        print "After reverse retruning: ", printList(r)
        return r

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == 1 and n ==1 :
            return head
        m = m - 1
        n = n - 1
        save = head
        m_head_prev = None
        m_head = head
        while m:
            m_head_prev = m_head
            m_head = m_head.next
            m = m - 1
            n = n - 1
        print "Head now at: ", m_head.val, " and n : ", n

        n_head = m_head
        while n:
            n_head = n_head.next
            n = n - 1

        print "n head now points to: ", n_head.val
        if (m_head_prev == None and n_head.next == None):
            return self.reverse(head)

        n_head_next = n_head.next
        n_head.next = None
        m_head_new = self.reverse(m_head)

        if m_head_prev is None:
            save = m_head_new
        else:
            m_head_prev.next = m_head_new
        m_head.next = n_head_next

        return save


print "Before"
q = getList([1, 2, 3, 4])
s = Solution()
assert (printList(s.reverseBetween(getList([1, 2, 3, 4]), 2, 4)) == [1, 4,3, 2])
assert (printList(s.reverseBetween(getList([3, 5]), 1, 2)) == [5, 3])
assert (printList(s.reverseBetween(getList([1, 2, 3]), 1, 2)) == [2, 1, 3])