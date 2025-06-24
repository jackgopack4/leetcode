func isMatch(s string, p string) bool {
    dp := make(map[[4]int]bool)
    var solve func(int,int,int,int) bool
    solve = func(sStart,sEnd,pStart,pEnd int) bool {
        var tmp bool
        if res, ok := dp[[4]int{sStart,sEnd,pStart,pEnd}]; ok {
            return res
        }
        if pStart > pEnd || pStart >= len(p) {
            tmp = sStart > sEnd || sStart >= len(s)
            dp[[4]int{sStart,sEnd,pStart,pEnd}] = tmp
            return tmp
        }
        firstCharMatches := sStart < len(s) && 
            (p[pStart] == s[sStart] || p[pStart] == '.')
        if pEnd > pStart && p[pStart+1] == '*' {
            tmp = solve(sStart, sEnd, pStart+2, pEnd) ||
                firstCharMatches && solve(sStart+1, sEnd, pStart, pEnd)
            dp[[4]int{sStart,sEnd,pStart,pEnd}] = tmp
            return tmp
        }
        tmp = firstCharMatches && solve(sStart+1, sEnd, pStart+1, pEnd)
        dp[[4]int{sStart,sEnd,pStart,pEnd}] = tmp
        return tmp
    }
    return solve(0,len(s)-1,0,len(p)-1)
}
