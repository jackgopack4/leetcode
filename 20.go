func isValid(s string) bool {
    closeMap := make(map[byte]byte)
    closeMap['('] = ')'
    closeMap['{'] = '}'
    closeMap['['] = ']'
    stack := []byte{}
    for _, c := range s {
        cByte := byte(c)
        if len(stack) == 0 {
            // must be open-paren
            if _, ok := closeMap[cByte]; !ok {
                return false
            } else {
                stack = append(stack, cByte)
            }
        } else {
            // if adding open-paren, good to go
            // else, if closing, must match
            if _, ok := closeMap[cByte]; !ok { // we know it's not an open paren
                if last, ok2 := closeMap[stack[len(stack)-1]]; ok2 {
                    if last != cByte {
                        return false
                    }
                    stack = stack[:len(stack)-1]
                } // don't need an else because if it's a close paren, it's in the map
            } else { // must be open parn, add to stack
                stack = append(stack, cByte)
            }
        }
    }
    if len(stack) != 0 {
        return false
    }
    return true
}
