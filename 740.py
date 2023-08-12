class Solution:
    
    def deleteAndEarn(self, nums: List[int]) -> int:
        def preProcess(nums: List[int]) -> List[int]:
            nums.sort()
            maxVal = nums[-1]
            processed = [0]*(maxVal+1)
            prev = nums[0]
            tmp = 0
            i = 0
            j = 0
            while i <= maxVal and j < len(nums):
                if nums[j] == i:
                    processed[i]+=i
                    j+=1
                else:
                    i+=1
            return processed
        nums2 = preProcess(nums)
        dp = [0]*len(nums2)
        for i in range(len(nums2)):
            if i == 0:
                dp[0] = nums2[0]
            elif i == 1:
                dp[1] = max(dp[0],nums2[1])
            else:
                dp[i] = max(nums2[i]+dp[i-2],dp[i-1])
        return dp[len(nums2)-1]
