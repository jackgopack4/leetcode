func generateParenthesis(n int) []string {
    // idea - recurse based on current partial string and number of remaining L/R parens
    // can probably memoize/DP from there.
    res := make(map[string]bool)
    var build func([]byte, int, int)
    build = func(s []byte, l, r int) {
        if l == 0 && r == 0 {
            b := strings.Builder{}
            b.Write(s)
            res[b.String()] = true
            return
        }
        // should never happen but add for safety
        if len(s) == 0 {
            panic("build should only be called with non-empty byte array")
        }
        // we can add lp or rp to this
        // can only add rp if lp < rp
        if l > 0 {
            build(append(s,'('), l-1, r)
        }
        if l < r {
            if r > 0 {
                build(append(s,')'), l, r-1)
            }
        }
    }
    build([]byte{'('}, n-1, n)
    pairs := make([]string, len(res))
    i := 0
    for k := range res {
        pairs[i] = k
        i += 1
    }
    return pairs
}
