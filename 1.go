import "slices"
func twoSum(nums []int, target int) []int {
    sortedNums := make([]int, len(nums))
    copy(sortedNums, nums)
    // sort then two pointer approach
    slices.Sort(sortedNums)
    lp, rp := 0, len(nums)-1
    for {
        tmp := sortedNums[lp] + sortedNums[rp]
        if tmp == target {
            res := []int{}
            for i, v := range nums {
                if v == sortedNums[lp] || v == sortedNums[rp] {
                    res = append(res, i)
                }
            }
            return res
        }
        if tmp < target {
            lp += 1
        } else {
            rp -= 1
        }
        if lp >= rp {
            panic("cannot happen, provide a valid nums/target combo")
        }
    }
}
