__author__ = 'deepika'


class Solution:

    def numberOfOptions(self, priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars):

        num_of_ways = 0
        return self.numberOfOptionsUtil(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars, num_of_ways)

    def numberOfOptionsUtil(self, priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars, num_of_ways):

        arrays = [priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops]

        n = len(arrays)

        indices = [0] * n

        while True:

            count = 0
            result = []
            for i in range(n):
                result.append(arrays[i][indices[i]])
                count += arrays[i][indices[i]]
                if count > dollars:
                    break
            if len(result) > 0:
                print(result)

            if count <= dollars:
                num_of_ways += 1

            nextArray = n - 1

            # Basically check if there is any indices[i] left to be processed.
            while nextArray >= 0 and indices[nextArray] + 1 >= len(arrays[nextArray]):
                nextArray -= 1

            if nextArray < 0:
                break

            indices[nextArray] += 1

            for i in range(nextArray + 1, n):
                indices[i] = 0

        return num_of_ways

s=Solution()
print(s.numberOfOptions(priceOfJeans = [2, 3],
priceOfShoes = [4],
priceOfSkirts = [2, 3],
priceOfTops = [1, 2],
dollars = 10))