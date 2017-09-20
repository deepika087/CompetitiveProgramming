__author__ = 'deepika'


class Solution(object):

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        numbers = [str(x) for x in range(1, n+1)]

        def less_than(x, y):
            return x < y


        def make_comparator():
            def compare(x, y):
                if less_than(x, y):
                    return -1
                elif less_than(y, x):
                    return 1
                else:
                    return 0
            return compare

        numbers = sorted(numbers, cmp=make_comparator())
        numbers = [int(x) for x in numbers]
        return numbers

s=Solution()
print s.lexicalOrder(13)