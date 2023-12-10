class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45:
            return []
        # need helper function that takes in index of remaining numbers and number left
        # and target sum
        initial_nums = [9,8,7,6,5,4,3,2,1]
        res = []
        def helper(current_sol, next_index, k, n):
            nonlocal res
            if next_index > 8:
                return
            if k == 1:
                if n > initial_nums[next_index] or n == 0:
                    return
                res.append(current_sol+[n])
                return
            for i in range(next_index,9):
                if initial_nums[i] < n:
                    helper(current_sol+[initial_nums[i]],i+1,k-1,n-initial_nums[i])
        helper([],0,k,n)
        return res
