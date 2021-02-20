__author__ = 'deepika'

"""
Runtime: 416 ms, faster than 39.58% of Python online submissions for Most Profit Assigning Work.
Memory Usage: 18.5 MB, less than 5.21% of Python online submissions for Most Profit Assigning Work.
"""

class Job:
    def __init__(self, d, p):
        self.diff = d
        self.money = p

    def __repr__(self):
        return str(self.diff) + ", " + str(self.money)

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):


        if len(difficulty) == 0:
            return 0

        jobs = []
        for i in range(len(difficulty)):
            jobs.append(Job(difficulty[i], profit[i]))

        jobs = sorted(jobs, key=lambda x:x.diff)

        for i in range(1, len(jobs)):
            jobs[i].money = max(jobs[i-1].money, jobs[i].money)

        worker = sorted(worker)
        k = 0
        result = 0

        for i in range(0, len(worker)):
            while k < len(jobs) and jobs[k].diff <= worker[i]:
                k += 1

            if k >= len(jobs):
                k = k-1
            if jobs[k].diff <= worker[i]:
                result += jobs[k].money
            elif k-1 >= 0 and jobs[k-1].diff <= worker[i]:
                result += jobs[k-1].money
        return result

s=Solution()
assert s.maxProfitAssignment([23,30,35,35,43,46,47,81,83,98], [8,11,11,20,33,37,60,72,87,95], [95,46,47,97,11,35,99,56,41,92]) == 553
assert  s.maxProfitAssignment([13,37,58], [4,90,96], [34,73,45]) == 190
assert s.maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]) == 100
assert s.maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [50,20,30,40,10], worker = [4,5,6,7]) == 200




