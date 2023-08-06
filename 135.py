# 135. Candy (this solution doesn't work but saving my work)
class ListNode(object):
    def __init__(self, rating=0, candy=1, right=None, left=None):
        self.rating = rating
        self.candy = candy
        self.right = right
        self.left = left
class Solution(object):
    def __init__(self):
        self.head = ListNode()
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) == 1:
            return 1
        
        self.head = ListNode(rating=ratings[0])
        cur = self.head
        for i in range(1,len(ratings)):
            cur.right = ListNode(rating=ratings[i])
            prev = cur
            cur = cur.right
            cur.left = prev
        cur = self.head
        while cur != None:
            # if ranking lower than left, must have less than left
            # if ranking higher than left, must have more than left
            # if ranking lower than right, must have less than right
            # if ranking higher than right, must have more than right
            
            if cur.left != None:
                if cur.left.rating < cur.rating and cur.candy <= cur.left.candy:
                    cur.candy = cur.left.candy+1
                if cur.left.rating > cur.rating and cur.left.candy <= cur.candy:
                    cur.left.candy=cur.candy+1
            if cur.right != None:
                if cur.right.rating < cur.rating and cur.candy <= cur.right.candy:
                    cur.candy = cur.right.candy+1
                if cur.right.rating > cur.rating and cur.right.candy <= cur.candy:
                    cur.right.candy=cur.candy+1
            cur = cur.right
        cur = self.head
        candies = 0
        while cur != None:
            print("cur rating: %d cur candy: %d" % (cur.rating, cur.candy))
            candies+=cur.candy
            cur = cur.right
        return candies
