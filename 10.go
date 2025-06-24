func isMatch(s string, p string) bool {
    if len(p) == 0 {
        return len(s) == 0
    }
    firstCharMatches := len(s) > 0 && (p[0] == s[0] || p[0] == '.')
    if len(p) > 1 && p[1] == '*' {
        return isMatch(s, p[2:]) || firstCharMatches && isMatch(s[1:], p)
    }
    return firstCharMatches && isMatch(s[1:],p[1:])
}
