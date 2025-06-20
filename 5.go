func longestPalindrome(s string) string {
    res := ""
    for i:=0; i < len(s); i++ {
        odd := longestSubPalindrome(i, i, s)
        if len(odd) > len(res) {
            res = odd
        }
        even := longestSubPalindrome(i, i+1, s)
        if len(even) > len(res) {
            res = even
        }
    }
    return res
}
func longestSubPalindrome(i, j int, s string) string {
    l := i
    r := j

    for l >= 0 && r < len(s) && s[l] == s[r] {
        l -= 1
        r += 1
    }

    return s[l+1 : r]
}
