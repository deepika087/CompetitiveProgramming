"""
This is a variation from Leetcode 973 cz in this case
if equal entities crash then they switch signs
[3,8,-2,-8]
Ans [-8,8]
Explanation : Up until -2, the problem is similar to question #1, but when we encounter -8,
because the number on the top of the stack is 8, when they collide, they both change
directions. -8 becomes 8 and the number on the top of the stack becomes -8 and
moves in the opposite direction and crushes everything with smaller weight
(and moving in opposite direction). So 3 in the stack gets crushed, resulting in [-8,8]
"""


class Solution(object):
    def isTravellingTowardsEachOther(self, incoming, top_of_stack):
        return incoming < 0 and top_of_stack > 0

    def asteroidCollision(self, asteroids):

        stack = []
        i = 0
        while i < len(asteroids):
            if len(stack) == 0:
                stack.append(asteroids[i])
                i += 1

            elif self.isTravellingTowardsEachOther(asteroids[i], stack[-1]):
                if abs(asteroids[i]) == abs(stack[-1]):
                    popped = stack.pop()
                    asteroids[i-1] = -popped # i-1 will always be greater than zero
                    i = i - 1
                    continue
                elif abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                else:
                    i += 1
                    continue
            else:
                stack.append(asteroids[i])
                i += 1

        return stack


s=Solution()
print(s.asteroidCollision([3,8,-2,-8]))
print(s.asteroidCollision([6,2,4,-3,6,1,3,-5,-6, 4,-6]))