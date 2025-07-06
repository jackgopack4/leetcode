func letterCombinations(digits string) []string {
    if len(digits) == 0 {
        return []string{}
    }
    letters := make(map[byte][]byte)
    letters['2'] = []byte{'a','b','c'}
    letters['3'] = []byte{'d','e','f'}
    letters['4'] = []byte{'g','h','i'}
    letters['5'] = []byte{'j','k','l'}
    letters['6'] = []byte{'m','n','o'}
    letters['7'] = []byte{'p','q','r','s'}
    letters['8'] = []byte{'t','u','v'}
    letters['9'] = []byte{'w','x','y','z'}
    res := []string{}
    if len(digits) == 1 {
        for _, c := range letters[digits[0]] {
            res = append(res,string(c))
        }
        return res
    }
    if len(digits) == 2 {
        for _, c := range letters[digits[0]] {
            for _, d := range letters[digits[1]] {
                res = append(res,string(c)+string(d))
            }
        }
        return res
    }
    if len(digits) == 3 {
        for _, c := range letters[digits[0]] {
            for _, d := range letters[digits[1]] {
                for _, e := range letters[digits[2]] {
                    res = append(res,string(c)+string(d)+string(e))
                }
            }
        }
        return res
    }
    if len(digits) == 4 {
        for _, c := range letters[digits[0]] {
            for _, d := range letters[digits[1]] {
                for _, e := range letters[digits[2]] {
                    for _, f := range letters[digits[3]] {
                        res = append(res,string(c)+string(d)+string(e)+string(f))
                    }
                }
            }
        }
        return res
    }
    return res
}
