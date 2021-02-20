__author__ = 'deepika'


def subset_k(a, s, i, k):
    if k == 0:
        print(s)
        return

    for p, q in enumerate(a):
        s[i] = q
        subset_k(a[p+1:], s, i + 1, k - 1)

#subset_k(range(4), [0] * 2, 0, 2)

def permuteK(setInput, k) :
    n = len(setInput)
    resultSet = []
    printAllKLengthRecprintAllKLengthRec(setInput, "", n, k, resultSet)
    print resultSet

def printAllKLengthRecprintAllKLengthRec(setInput, prefix, n, k, resultSet) :

    if (k == 0):
        resultSet.append(prefix);
        return;

    #// One by one add all characters from set and recursively
    #// call for k equals to k-1
    for i in range(n):
        printAllKLengthRecprintAllKLengthRec(setInput, prefix + str(setInput[i]), n, k - 1, resultSet);

#permuteK(range(4), 2)

def subsetsWithDupUtil(nums, prefix, index, results):
    if index == 0:
        results.append(prefix)
        return results

    for i in range(len(nums)):
        subsetsWithDupUtil(nums, prefix + str(nums[i]), index - 1, results)

results = []
#print subsetsWithDupUtil([1, 2, 3], "", 3 , results)
#print results

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        resultsCount=[]
        pos=0
        currSet = []
        self.combinationSum4Util(nums, target, pos, currSet, resultsCount)
        return len(resultsCount)

    def combinationSum4Util(self, nums, target, pos, currSet, resultsCount):
        #print "currSet: ", currSet
        if sum(currSet) > target:
            return
        if sum(currSet) == target:
            #print "adding for currSet: ", currSet
            
            resultsCount.append(currSet)
            #print "Result count is now: ", resultsCount
            return resultsCount

        i = 0
        while i < len(nums):
            if nums[i] > target:
                continue
            currSet.append(nums[i])
            self.combinationSum4Util(nums, target, i + 1, currSet, resultsCount)
            currSet.pop(-1)
            i = i + 1
        return resultsCount

s=Solution()
print s.combinationSum4([1, 2, 3], 4)

