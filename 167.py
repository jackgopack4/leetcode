class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0,len(numbers)-1
        while lp < rp:
            temp_sum = numbers[lp]+numbers[rp]
            if temp_sum == target:
                return [lp+1,rp+1]
            elif temp_sum < target:
                lp += 1
            else:
                rp -= 1
        return [-1,-1]
