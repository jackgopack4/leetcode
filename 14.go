func longestCommonPrefix(strs []string) string {
    res := ""
    idx := 0
    for {
        if idx >= len(strs[0]) {
            break
        }
        cur := strs[0][idx]
        match := true
        for i := 1; i < len(strs); i++ {
            if idx >= len(strs[i]) || strs[i][idx] != cur {
                match = false
                break
            }
        }
        if match {
            res += string(cur)
        } else {
            break
        }
        idx += 1
    }
    return res
}
