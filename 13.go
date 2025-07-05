func romanToInt(s string) int {
    chars := []byte{
        'I',
        'V',
        'X',
        'L',
        'C',
        'D',
        'M',
    }
    vals := []int{1, 5, 10, 50, 100, 500, 1000}
    charVals := make(map[byte]int)
    for i, c := range chars {
        charVals[c] = vals[i]
    }
    suffixes := make(map[byte][]byte)
    suffixes['I'] = []byte{'V', 'X'}
    suffixes['X'] = []byte{'L', 'C'}
    suffixes['C'] = []byte{'D', 'M'}
    lp := 0
    rp := 1
    res := 0
    for {
        if lp >= len(s) {
            break
        }
        if rp < len(s) {
            // need to check for I, X, or C
            suf, ok := suffixes[s[lp]]
            if ok {
                found := false
                for _, c := range suf {
                    if s[rp] == c {
                        res += charVals[s[rp]] - charVals[s[lp]]
                        lp += 2
                        rp += 2
                        found = true
                        break
                    }
                }
                if !found {
                    res += charVals[s[lp]]
                    lp += 1
                    rp += 1
                }
            } else {
                res += charVals[s[lp]]
                lp += 1
                rp += 1
            }
        } else {
            res += charVals[s[lp]]
            lp += 1
        }
    }
    return res
}
