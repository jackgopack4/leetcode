# 135. Candy (no more linkedlist, maybe faster?)
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)
        if length == 1:
            return 1
        candies = [1] * length
        for i in range(length):
            if i+1 < length:
                if ratings[i+1] < ratings[i] and candies[i+1] >= candies[i]:
                    candies[i] = candies[i+1]+1
                if ratings[i+1] > ratings[i] and candies[i+1] <= candies[i]:
                    candies[i+1] = candies[i]+1
        for i in range(length-1,-1,-1):
            if i-1 >= 0:
                if ratings[i-1] < ratings[i] and candies[i-1] >= candies[i]:
                    candies[i] = candies[i-1]+1
                if ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
                    candies[i-1] = candies[i]+1
        return sum(candies)
