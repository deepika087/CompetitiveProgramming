import sys
"""
18 / 18 test cases passed.
Status: Accepted
Runtime: 202 ms

Main Point to note was to resuse the holes left by popping.
Just appending None will not work. becuase then when you invoke append
size of the list increases
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minstack=[]
        self.ptr = -1

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.ptr = self.ptr + 1
        if (self.ptr < len(self.stack)):
            self.stack[self.ptr]=x
            if(self.ptr==0):
                self.minstack[self.ptr]=x
            else:
                self.minstack[self.ptr]=min(x, self.minstack[self.ptr-1])
        else:
            self.stack.append(x)
            if(self.ptr==0):
                self.minstack.append(x)
            else:
                temp=min(self.minstack[self.ptr-1], x)
                self.minstack.append(temp)

    def pop(self):
        """
        :rtype: void
        """
        if (self.ptr < 0):
            return "null"
        item=self.stack[self.ptr]
        self.stack[self.ptr]=None
        self.minstack[self.ptr]=None
        self.ptr=self.ptr-1
        return item


    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.ptr]

    def getMin(self):
        """
        :rtype: int
        """
        if (self.ptr < 0):
            return "null"
        #print "Ptr is at ", self.ptr
        return self.minstack[self.ptr]



# Your MinStack object will be instantiated and called as such:

line1=["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
line2=[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
#line1=line1.split(",")
#line2=line2.split(",")

print sys.maxint
obj=None
result=[]
for i in range(len(line1)):
    print "at i = ", i
    if (i==11):
        print line1[i], obj.stack, obj.minstack
    if(line1[i]=="MinStack"):
        obj = MinStack()
        print "constructor"
        result.append("constructor")
    elif(line1[i]=="push"):
        obj.push(line2[i])
        print "null"
        result.append("null")
    elif(line1[i]=="pop"):
        item = obj.pop()
        result.append("null")

    elif(line1[i]=="top"):
        result.append(obj.top())
        print " Top : ", obj.top()
    else:
        item=obj.getMin()
        result.append(item)
        print " Min : ", item
print result
