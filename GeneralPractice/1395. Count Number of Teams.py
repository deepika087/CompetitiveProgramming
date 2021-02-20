__author__ = 'deepika'


"""
This approach is wrong because practically you have fixed i.
Also, the sliding window approach won't work here.
Because say the input is 2, 5, 3, 10, 4, 1

Scan: 2, stack : 2
Scan: 5, stack : 2, 5
Scan: 3, stack  2, 5, 3 -> 2, 3
Scan: 10, stack should be 2, 5, 3 for the correct count rather than 2, 3

and now you are only finding k combos with j

there is no other way except to follow brute force and check each and every comparision
This approach is better. Precompute number of elements that are greater than every i.

class Solution {
    public int numTeams(int[] rating) {
        int n = rating.length;
        int[] gre = new int[n], low = new int[n];
        for(int i =0;i < n-1;i++) {
            int l = 0, h = 0;
            for(int j = i+1;j < n;j++) {
                if(rating[j] > rating[i]) h++;
                if(rating[j] < rating[i]) l++;
            }
            gre[i] = h;low[i] = l;
        }
        int count = 0;
        for(int i = 0;i < n-2;i++) {
            for(int j = i+1;j < n-1;j++) {
                if(rating[j] > rating[i]) {
                    count += gre[j];
                }else if(rating[j] < rating[i]) {
                    count += low[j];
                }
            }
        }
        return count;
    }
}
"""
class Solution(object):
    def numTeams(self, rating):

        stack = []
        stack.append(0)
        lessthan = [ 0 ] * len(rating)

        for i in range(len(rating)):
            if rating[i] > rating[stack[-1]]:
                stack.append(i)
            else:
                lessthan[i] = len(stack)
        print(lessthan)

        lessthan = [ 0 ] * len(rating)
        stack = []
        stack.append(len(rating)-1)
        for i in range(len(rating)-2, -1, -1):
            if rating[i]



    def numTeamsNotWorking(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        left_min = [ i for i in range(len(rating))]
        left_max = [ i for i in range(len(rating))]

        for i in range(1, len(rating)):
            left_min[i] = left_min[i-1] if rating[left_min[i-1]] < rating[i] else i
            left_max[i] = left_max[i-1] if rating[left_max[i-1]] > rating[i] else i

        count = 0
        for i in range(len(rating)):
            if left_min[i] != i:
                target = rating[i]

                for k in range(i+1, len(rating)):
                    if target < rating[k]:
                        assert rating[left_min[i]] < rating[i] < rating[k]
                        count += 1

        for i in range(len(rating) -1, -1, -1):
            if left_max[i] != i:

                target = rating[i]

                for k in range(i-1, -1, -1):
                    if target > rating[k]:
                        assert rating[left_max[i]] > rating[i] > rating[k]
                        count += 1
        return count

s=Solution()
print(s.numTeams(rating = [2,5,3,4,1]))

print(s.numTeams(rating = [2,1,3]))

print(s.numTeams(rating = [1,2,3,4]))