func fourSum(nums []int, target int) [][]int {
    slices.Sort(nums)
    resMap := make(map[[4]int]bool)
    res := [][]int{}
    // for each n in nums, solve three-sum to the right of it
    // where 3-target = target - n
    var threeSumFunc func(int, int)
    threeSumFunc = func(startIdx int, threeTarget int) {
        for j := startIdx; j < len(nums) - 2; j++ {
            lp, rp := j + 1, len(nums)-1
            for {
                if lp >= rp {
                    break
                }
                tmpSum := nums[j] + nums[lp] + nums[rp]
                if tmpSum == threeTarget {
                    tmpArray := [4]int{
                        nums[startIdx-1],
                        nums[j],
                        nums[lp],
                        nums[rp],
                    }
                    if _, ok := resMap[tmpArray]; !ok {
                        resMap[tmpArray] = true
                        res = append(res, []int{
                            nums[startIdx-1],
                            nums[j],
                            nums[lp],
                            nums[rp],
                        })
                    }
                    lp += 1
                    rp -= 1
                } else if tmpSum < threeTarget {
                    lp += 1
                } else { // tmpSum > threeTarget
                    rp -= 1
                }
            }
        }
    }
    for i, n := range nums {
        threeSumFunc(i+1, target-n)
    }
    return res
}
