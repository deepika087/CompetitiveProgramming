__author__ = 'deepika'

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))

        if len(num) in [0, 1]:
            return int(''.join(num))

        old_part = ''
        while len(num) > 0:
            max_i = num.index(max(num))
            if max_i == 0:
                old_part += num[0]
                num = num[1:]
                continue

            min_i = num.index(min(num[0:max_i]))
            num[max_i], num[min_i] = num[min_i], num[max_i]
            break
        return int(''.join(old_part + ''.join(num)))

s=Solution()
assert s.maximumSwap(2736) == 7236
assert s.maximumSwap(9973) == 9973
assert s.maximumSwap(98368) == 98863