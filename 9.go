func isPalindrome(x int) bool {
    if x == 0 {
        return true
    }
    if x < 0 {
        return false
    }
    digits := make([]int, 0)
    var (
        remainder int
    )
    tmp := x
    for {
        if tmp == 0 {
            break
        }
        remainder = tmp % 10
        tmp = tmp / 10
        digits = append(digits, remainder)
    }
    for i, d := range digits {
        backIdx := len(digits) - 1 - i
        if backIdx <= i {
            return true
        }
        if d != digits[backIdx] {
            return false
        }
    }
    return true
}
