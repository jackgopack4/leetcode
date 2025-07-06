func threeSum(nums []int) [][]int {
    slices.Sort(nums)
    res := [][]int{}
    for i, n := range nums {
        if i-1 >= 0 && nums[i-1] == n {
            continue
        }
        // can't possibly add three positive numbers to get zero
        if n > 0 {
            break
        }
        // else, use lp, rp to find every other pair to right of index i that sums
        // with n to equal zero
        lp, rp := i+1, len(nums)-1
        for {
            if lp >= rp {
                break
            }
            // check if lp same as previous lp or rp same as previous rp
            if lp - 1 > i && nums[lp] == nums[lp - 1] {
                lp += 1
                continue
            }
            if rp + 1 < len(nums) && nums[rp] == nums[rp + 1] {
                rp -= 1
                continue
            }
            if nums[lp]+nums[rp]+n == 0 {
                res = append(res, []int{n,nums[lp],nums[rp]})
                lp += 1
                rp -= 1
            } else if nums[lp]+nums[rp]+n < 0 {
                lp += 1
            } else {
                rp -= 1
            }
        }
    }
    return res
}
