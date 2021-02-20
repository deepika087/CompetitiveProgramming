__author__ = 'deepika'

"""
Runtime: 2072 ms, faster than 42.20% of Python online submissions for Best Team With No Conflicts.
Memory Usage: 13.7 MB, less than 5.05% of Python online submissions for Best Team With No Conflicts.
"""
class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """

        combinedData = []
        for i in range(len((scores))):
            combinedData.append( [ages[i], scores[i]] )

        combinedData = sorted(combinedData, key=lambda x: (x[0], x[1]))
        #print(combinedData)

        ans = [ 0 for i in range(len(combinedData))]

        best = 0
        for i in range(len(combinedData)):
            ans[i] = combinedData[i][1]
            for j in range(0, i):
                if combinedData[i][1] >= combinedData[j][1]:
                    ans[i] = max(ans[i], ans[j] + combinedData[i][1])
            best = max(best, ans[i])
        return best

s=Solution()
assert s.bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5]) == 34
assert s.bestTeamScore( scores = [4,5,6,5], ages = [2,1,2,1]) == 16
assert s.bestTeamScore(scores = [1,2,3,5], ages = [8,9,10,1]) == 6