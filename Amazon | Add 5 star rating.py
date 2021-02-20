__author__ = 'deepika'


"""
Third-party companies that sell their products on Amazon.com are able to analyze the customer reviews for their products in real time. Imagine that Amazon is creating a category called "five-star sellers" that will only display products sold by companies whose average percentage of five-star reviews per-product is at or above a certain threshold. Given the number of five-star and total reviews for each product a company sells, as well as the threshold percentage, what is the minimum number of additional fivestar reviews the company needs to become a five-star seller?

For example, let's say there are 3 products (n = 3) where productRatings = [[4,4], [1,2], [3, 6]], and the percentage ratings Threshold = 77. The first number for each product in productRatings denotes the number of fivestar reviews, and the second denotes the number of total reviews. Here is how we can get the seller to reach the threshold with the minimum number of additional five-star reviews:

Before we add more five-star reviews, the percentage for this seller is ((4 / 4) + (1/2) + (3/6))/3 = 66.66%
If we add a five-star review to the second product, the percentage rises to ((4 / 4) + (2/3) +(3/6))/3 = 72.22%
If we add another five-star review to the second product, the percentage rises to ((4 / 4) + (3/4) + (3/6))/3 = 75.00%
If we add a five-star review to the third product, the percentage rises to ((4/4) + (3/4) + (4/7))/3 = 77.38%
At this point, the threshold of 77% has been met. Therefore, the answer is 3 because that is the minimum number of additional five-star reviews the company needs to become a five-star seller.


The idea is that create a priority queue with the diff as key and index as value.
diff = difference in the ratio is we increase the numerator and denominator of productRating[i]

Initially, put only those elements in the priority queue for which the current rating is not 100% for ex [4, 4]
will be ignored.

Next, every time you pop from heap, increment number of reviews required and put back the new diff and the index.
"""
import heapq

class Solution:

    def fetch_current_rating(self, productRating):

        curr_rating = 0

        for pr in productRating:
            curr_rating += pr[0] * 1.0/pr[1]

        return curr_rating*100.0/len(productRating)


    def addRating(self, productRatings, threshold):

        pq = []

        n = len(productRatings)

        number_of_increments = 0

        for i in range(n):
            pr = productRatings[i]

            if pr[0] != pr[1]:
                new_numerator = pr[0] + 1
                new_denominator = pr[1] + 1

                diff = (new_numerator * 1.0/new_denominator - pr[0]* 1.0/pr[1])
                print("Diff for index i: ", i, " is ", diff)

                heapq.heappush(pq, [-diff,  i] )

        while pq and self.fetch_current_rating(productRatings) < threshold:
            popped = heapq.heappop(pq)
            index = popped[1]

            productRatings[index][0] += 1
            productRatings[index][1] += 1

            new_numerator = productRatings[index][0]  + 1
            new_denominator = productRatings[index][1] +  1

            diff = (new_numerator * 1.0/new_denominator -  productRatings[index][0] * 1.0/productRatings[index][1])

            heapq.heappush(pq, [-diff,  index] )

            number_of_increments += 1
        return number_of_increments

s=Solution()
print(s.addRating([[4,4], [1,2], [3, 6]], 77))







