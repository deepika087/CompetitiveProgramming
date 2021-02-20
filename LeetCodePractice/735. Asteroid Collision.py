__author__ = 'deepika'

"""
Runtime: 88 ms, faster than 27.79% of Python online submissions for Asteroid Collision.
Memory Usage: 14.5 MB, less than 68.56% of Python online submissions for Asteroid Collision.

Time: O(n)
Space: O(n)
"""
class Solution(object):
    def isTravellingInOppositeDirection(self, a, b):
        return a < 0 and b > 0

    def asteroidCollision(self, asteroids):

        stack = []
        i = 0
        while i < len(asteroids):
            if len(stack) == 0:
                stack.append(asteroids[i])
                i += 1

            elif self.isTravellingInOppositeDirection(asteroids[i], stack[-1]):
                if abs(asteroids[i]) == abs(stack[-1]):
                    stack.pop()
                    i += 1
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

print s.asteroidCollision([-2,-2,-2,-2])
print s.asteroidCollision([5, -5])
print s.asteroidCollision([-5, 5])
print s.asteroidCollision([10, 2, -5])
print s.asteroidCollision([5, 10, -5])
print s.asteroidCollision([6, 2, 5, -10])
print s.asteroidCollision([-6, -2, -5, 10])
print s.asteroidCollision([-2, -1, 1, 2])
