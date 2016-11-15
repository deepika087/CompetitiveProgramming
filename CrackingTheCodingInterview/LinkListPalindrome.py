

class Node(object):
    def __init__(self, _data):
        self.data=_data
        self.next=None

class LinkList(object):
    def __init__(self):
        self.head=None
        self.left=None

    def printList(self):
        temp_head=self.head
        while(temp_head is not None):
            print temp_head.data + " ->"
            temp_head=temp_head.next

    def isPallindrome(self):
        return self.isPallindromeUtil(ll.head)

    def isPallindromeUtil(self, right):
        self.left=self.head

        if (right is None):
            return True

        result=self.isPallindromeUtil(right.next)
        if(not result):
            return result

        print " Comparing ", self.left.data, " and ", right.data
        result1=ord(self.left.data) == ord(right.data)
        self.left=self.left.next

        return result1

if __name__=="__main__":

    ll=LinkList()

    input="abbcbba"
    temp_head=None
    for i in range(len(input)):
        if (i == 0):
            ll.head=Node(input[i])
            temp_head=ll.head
        else:
            temp_head.next=Node(input[i])
            temp_head=temp_head.next

    ll.printList()
    print ll.isPallindrome()

