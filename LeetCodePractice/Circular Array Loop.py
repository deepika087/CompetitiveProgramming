"""
Failing  1 test case [-1, -2, -3, -4, -5 ]
9/10 pass
"""
class Solution(object):
    def checkIfReal(self, nums, start):
        count = 0
        save=start
        Forward = 0
        BackWard = 0
        while(True):
            if (nums[start] > 0):
                end = (start + nums[start])%len(nums)
                if (end > start):
                    count = count + end - start + 1
                    #Forward = count
                elif ( end < start):
                    count = count + len(nums) - start
                    count = count + end
                    #Forward = count
                else:
                    count = count + len(nums) - 1
                Forward=count
                #count = count + (end-start + 1 if end > start else 1)
                Forward = Forward + 1
                if (save == end):
                    if (count <= 1):
                        return False
                    elif (Forward > 1 and BackWard <= 1):
                        return True
                    else:
                        #print " Because of or condition"
                        return False
            else:
                # = BackWard + 1
                temp = start + nums[start]
                if ( temp < 0):
                    end = len(nums) + temp
                else:
                    end = start + nums[start]

                if (end > start):
                    count = count + end - start + 1
                    #Forward = count
                elif ( end < start):
                    count = count + len(nums) - start
                    count = count + end
                else:
                    count = count + len(nums) - 1
                BackWard = count
                if (save == end):

                    if (count <= 1):
                        return False
                    elif (BackWard > 1 and Forward <= 1):
                        return True
                    else:

                        return False
            start=end
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        checker = 0
        while ( i >= 0 and i < len(nums)):
            if (checker & 1 << i > 0):
                return self.checkIfReal(nums, i )

            checker=checker | 1 << i
            if (nums[i] > 0):
                i = (i + nums[i]) % len(nums)
            else:
                temp=i + nums[i]
                if ( temp < 0):
                    i = len(nums) + temp
                else:
                    i = i + nums[i]
        return False

s=Solution()
print s.circularArrayLoop([-1, -2, -3, -4, -5]) #Expected False
print s.circularArrayLoop([1, -2]) #Expected False
print s.circularArrayLoop([3,1,2])  #Expected true
print s.circularArrayLoop([2, -1, 1, -2, -2]) #Expected False
print s.circularArrayLoop([2, -1, 1, 2, 2])  #Expected False
print s.circularArrayLoop([-1, 2]) #Expected False