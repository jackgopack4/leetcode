func twoSum(nums []int, target int) []int {
    tmp := make(map[int]int)
    for idx1, n := range nums {
        if idx2, ok := tmp[target - n]; ok {
            return []int{idx1, idx2}
        }
        tmp[n] = idx1
    }
    return []int{0,0}
}
