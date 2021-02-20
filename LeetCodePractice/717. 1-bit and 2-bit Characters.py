__author__ = 'deepika'

"""
Accepted in contest, so cann't see ranking
"""

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        #Assume that it is true.subs
        return self.is_valid(bits[0:len(bits)-1])

    def is_valid(self, bits):
        if len(bits) == 0:
            return True
        if len(bits) == 1:
            if bits[0] == 0:
                return True
            else:
                return False
        if len(bits) == 2:
            if bits == [1, 1] or bits == [1, 0]:
                return True
            if bits == [0, 0]:
                return True
            return False #[0, 1]
        else:
            lastChar = bits[-1]
            secondLastChar = bits[-2]
            if lastChar == 1 and secondLastChar == 0:
                return False
            if lastChar == 1:
                return self.is_valid(bits[0:len(bits) - 2])
            else: #lastChar == 0
                return self.is_valid(bits[0:len(bits) - 1]) \
                    or self.is_valid(bits[0:len(bits) - 2]) #considering it part of 10
s=Solution()
assert s.isOneBitCharacter([1, 0, 0]) == True
assert s.isOneBitCharacter([1, 1, 1, 0]) == False
assert s.isOneBitCharacter([1, 0, 1, 1, 1, 0, 1, 1, 0]) == True
assert s.isOneBitCharacter([0, 0, 0]) == True
assert s.isOneBitCharacter([0,0,1,0]) == False