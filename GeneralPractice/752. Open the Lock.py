__author__ = 'deepika'


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        dead = set(deadends)
        if "0000" in dead:
            return -1
        q = [("0000", 0)]
        dead.add("0000")
        while len(q) > 0:
            key, dis = q.pop(0)
            print(key)
            if key == target:
                return dis

            neigh = self.getNeigh(key, dead, dis+1)
            if len(neigh) > 0:
                q.extend(neigh)
        return -1


    def getNeigh(self, state, dead, dis):
        output = []
        for i in range(4):
            num = int(state[i])
            for a in ((num-1), (num+1)):
                tmp = state[:i] + str(a%10) + state[i+1:]
                if tmp not in dead:
                    output.append((tmp, dis))
                    dead.add(tmp)


        return output

s=Solution()
print(s.openLock(["0201","0101","0102","1212","2002"], "0202") )

