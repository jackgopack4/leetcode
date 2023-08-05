# 2476. Closest Nodes Queries in a Binary Search Tree

# You are given the root of a binary search tree and an array of queries of 
# size n consisting of positive integers.

# Find a 2D array answer of size n where answer[i] = [mini, maxi]:

# mini is the largest value in the tree that is smaller than or equal to 
# queries[i]. If such a value does not exist, add -1 instead.
# maxi is the smallest value in the tree that is greater than or equal to 
# queries[i]. If such a value does not exist, add -1 instead.
# Return the array answer.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def depthFirstTraversal(self,cur,stack):
        if cur != None:
            self.depthFirstTraversal(cur.left,stack)
            stack.append(cur.val)
            self.depthFirstTraversal(cur.right,stack)
    def binarySearch(self,query,stack):
        l = 0
        r = len(stack) - 1
        while r >= l:
            m = (l + r) // 2
            if stack[m] == query:
                return [query,query]
            elif stack[m] > query:
                if m == 0:
                    return [-1,stack[m]]
                elif stack[m-1] < query:
                    return [stack[m-1],stack[m]]
                else:
                    r = m-1
            else:
                if m == len(stack)-1:
                    return [stack[m],-1]
                elif stack[m+1] > query:
                    return [stack[m],stack[m+1]]
                else:
                    l = m+1
    def closestNodes(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[List[int]]
        """
        stack = []
        discovered = {}
        cur = root
        self.depthFirstTraversal(cur,stack)
        res = []
        for q in queries:
            res.append(self.binarySearch(q,stack))
        return res

        
    
