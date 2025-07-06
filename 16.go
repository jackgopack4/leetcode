func threeSumClosest(nums []int, target int) int {
    slices.Sort(nums)
    closestPos := math.MaxInt
    closestNeg := math.MinInt
    for i, n := range nums {
        if i-1 >= 0 && nums[i-1] == n {
            continue
        }
        lp, rp := i+1, len(nums)-1

        for {
            if lp >= rp {
                break
            }
            cur := n + nums[lp] + nums[rp] - target
            if cur == 0 {
                return target
            }
            if cur < 0 {
                if cur > closestNeg {
                    closestNeg = cur
                }
                lp += 1
            } else {
                if cur < closestPos {
                    closestPos = cur
                }
                rp -= 1
            }
        }
    }
    if -1*closestPos < closestNeg {
        return target + closestNeg
    } else {
        return target + closestPos
    }
}
