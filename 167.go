func twoSum(numbers []int, target int) []int {
    lp, rp := 0, len(numbers)-1
    for {
        if lp >= rp {
            break
        }
        sum := numbers[lp]+numbers[rp]
        if sum == target {
            return []int{lp+1, rp+1}
        }
        if sum < target {
            lp += 1
        } else {
            rp -= 1
        }
    }
    return []int{0, 0}
}
