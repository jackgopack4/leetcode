# Backtracking
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def helper(cur_list,visited,nums):
            nonlocal res
            if len(cur_list) == len(nums):
                res.append(cur_list)
            else:
                for n in nums:
                    if n not in visited:
                        visited.add(n)
                        helper(cur_list+[n],visited,nums)
                        visited.remove(n)
        helper([],visited,nums)
        return res
