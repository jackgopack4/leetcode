func intToRoman(num int) string {
    amounts := []int{1000, 900,  500, 400,  100, 90,   50,  40,   10,  9,    5,   4,   1}
    chars := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
    res := ""
    tmp := num
    for {
        if tmp == 0 {
            break
        }
        for i := 0; i < len(amounts); i++ {
            if tmp >= amounts[i] {
                tmp -= amounts[i]
                res += chars[i]
                break
            }
        }
    }
    return res
}
