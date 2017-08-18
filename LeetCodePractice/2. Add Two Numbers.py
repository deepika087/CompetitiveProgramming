__author__ = 'deepika'

# Definition for singly-linked list.
"""
1562 / 1562 test cases passed.
Status: Accepted
Runtime: 139 ms
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start, temp = None, None
        carry = 0
        while l1 or l2:
            data1 = l1.val if l1 else 0
            data2 = l2.val if l2 else 0

            new_node_data = data1 + data2 + carry
            carry = 1 if new_node_data >= 10 else 0
            if new_node_data >= 10:
                new_node_data = new_node_data%10
            if start is None:
                start = ListNode(new_node_data)
                temp = start
            else:
                temp.next = ListNode(new_node_data)
                temp = temp.next

            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        if carry:
            temp.next = ListNode(carry)
        return start

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

def printList(l1):
    result = []
    while l1:
        result.append(str(l1.val))
        l1 = l1.next
    result = '->'.join(result)
    print  result

l1=getList([2,4,3])
l2=getList([5,6,4])
printList(l1)
printList(l2)

s=Solution()
printList(s.addTwoNumbers(l1, l2))

l1=getList([5])
l2=getList([5])
printList(l1)
printList(l2)
printList(s.addTwoNumbers(l1, l2))

