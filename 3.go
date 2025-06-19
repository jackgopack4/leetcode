func lengthOfLongestSubstring(s string) int {
    // charMap is updated as window extends/contracts.
    // if a character is seen, increment right pointer. 
    // If that increment takes it to >1, increment left pointer until
    // it is reduced.
    // While this is happening, track longest substring seen yet.
    charMap := make(map[byte]int)
    if len(s) <= 1 {
        return len(s)
    }
    longestSeen, curLength := 1, 1
    incrementRight := true
    lp, rp := 0, 0
    charMap[s[lp]] = 1
    var char byte
    for {
        if incrementRight {
            rp += 1
            curLength += 1
            char = s[rp]
        } else {
            curLength -= 1
            char = s[lp]
            lp += 1
        }
        _, ok := charMap[char]
        if !ok {
            charMap[char] = 1
        } else {
            if incrementRight {
                charMap[char] += 1
            } else {
                charMap[char] -= 1
            }
        }
        if charMap[s[rp]] <= 1 {
            if curLength > longestSeen {
                longestSeen = curLength
            }
            if !incrementRight {
                incrementRight = true
            }
        } else {
            if incrementRight {
                incrementRight = false
            }
        }
        if incrementRight && rp >= len(s)-1 || !incrementRight && lp >= rp {
            return longestSeen
        }
    }
}
