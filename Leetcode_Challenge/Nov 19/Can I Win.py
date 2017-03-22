"""
464. Can I win
Not working solution
"""
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (desiredTotal == 0):
            return True
        if (desiredTotal % maxChoosableInteger == 0 and (desiredTotal/maxChoosableInteger)%2 == 0):
            return True
        result = [0 for i in range(desiredTotal)]
        pointer = len(result) - 1
        eff_sum = desiredTotal
        sum_so_far = 0
        while(True):
            #first player needs
            if(pointer == len(result) - 1):
                result[pointer] = 1
                sum_so_far = 1
                pointer = pointer - 1
            else:
                result[pointer] = maxChoosableInteger
                sum_so_far = sum_so_far + maxChoosableInteger
                pointer = pointer - 1

            if (sum_so_far >= desiredTotal):
                return True;

            if ( maxChoosableInteger <= desiredTotal - sum_so_far):
                result[pointer] = maxChoosableInteger
                sum_so_far = sum_so_far + maxChoosableInteger
                pointer = pointer - 1
            else:
                result[pointer] = desiredTotal - sum_so_far
                sum_so_far = sum_so_far + result[pointer]
                pointer = pointer - 1

            if (sum_so_far >= desiredTotal):
                return False



s=Solution()
print s.canIWin(10, 11)
print s.canIWin(10, 0)
print s.canIWin(10, 40)