__author__ = 'deepika'

"""
Taking too long.. though not a very difficult problem
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def getPointers(self, head, k):
        save_k = k
        if k == 0:
            return None
        start, k_node = head, head
        count = 1
        while k and k_node:
            count = count + 1
            k_node = k_node.next
            k = k - 1
            if k_node and k_node.next is None and k > 0:
                print "length found: ", count
                start, k_node = head, head
                k = save_k % count
                count = 1
                print "New k: ", k
                continue
        if not k_node:
            return head, None
        #print "k_node now points to(forward): ", k_node.val
        prev_k = start
        if save_k%2 == 1:
            start = start.next
        while k_node.next:
            #print " start now points to:", start.val, " -> ", k_node.val
            prev_k = start
            start = start.next
            k_node = k_node.next

        print "Kth node is : ", start.val
        print "k_node now points to(backward): ", k_node.val, " prev: ", prev_k.val
        return start, prev_k


    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return head
        if head is None:
            return []
        if head == []:
            #print "caught"
            return []
        k_node, prev_k = self.getPointers(head, k)
        #print "head: ", head.val, " k_node: ", k_node.val
        if (k_node == head):
            return head

        #print "k_th node: ", k_node.val
        prev_k.next = None
        #print "Node set to None: ", prev_k.val
        save_k = k_node
        while k_node.next:
            k_node = k_node.next
        k_node.next = head
        #print "k_node: ", k_node.val
        head = save_k
        return head

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

listNodes = getList([1, 2, 3, 4, 5, 6])
s=Solution()
"""
listNodes = s.rotateRight(listNodes, 2)
print "head now points tO;", printList(listNodes)
listNodes = s.rotateRight([], 1)
print "head now points tO;", printList(listNodes)
listNodes = s.rotateRight(getList([1]), 1)
print "head now points tO;", printList(listNodes)
listNodes = s.rotateRight(getList([1]), 99)
print "head now points tO;", printList(listNodes)
listNodes = s.rotateRight(getList([1, 2]), 1)
print "head now points tO;", printList(listNodes)
listNodes = s.rotateRight(getList([1, 2]), 3)
print "head now points tO;", printList(listNodes)
"""
listNodes = s.rotateRight(getList([1, 2, 3]), 2)
print "head now points tO;", printList(listNodes)