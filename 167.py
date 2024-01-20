class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers)-1
        while lp < rp:
            if numbers[lp]+numbers[rp] == target:
                return [lp+1,rp+1]
            elif numbers[lp]+numbers[rp] > target:
                rp -= 1
            else:
                lp += 1
        return [-1,-1]
