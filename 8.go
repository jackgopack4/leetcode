import "math"
func myAtoi(s string) int {
    if len(s) == 0 {
        return 0
    }
    dict := make(map[rune]int32)
    for i, c := range "0123456789-" {
        if i == 10 {
            dict[c] = int32(-1)
            continue
        }
        dict[c] = int32(i)
    }
    numSlice := make([]int32, len(s))
    idx := 0
    numberStarted := false
    digitsStarted := false
    numberIsNegative := false
    for _, c := range s {
        val, ok := dict[c]
        if !numberStarted {
            if c == ' ' {
                if digitsStarted {
                    return 0
                }
                continue
            }
            if c == '+' {
                if digitsStarted {
                    return 0
                }
                numberStarted = true
                continue
            }

            if !ok {
                return 0
            }
            if val == int32(-1) {
                if digitsStarted {
                    return 0
                }
                numberIsNegative = true
                digitsStarted = true
            } else {
                digitsStarted = true
                if val != int32(0) {
                    numberStarted = true
                }
                numSlice[idx] = val
                idx += 1
            }
        } else {
            if !ok || val == int32(-1) {
                if !numberStarted {
                    return 0
                }
                break
            }
            numSlice[idx] = val
            idx += 1
        }
    }
    lowerLimit := 0
    for i := 0; i < idx; i++ {
        if numSlice[i] == int32(0) {
            lowerLimit += 1
        } else {
            break
        }
    }
    // now we need to loop through digits in list and multiply
    mult := int32(1)
    multInt := 1
    res := int32(0)
    resInt := 0
    if (idx - lowerLimit) > 10 {
        if numberIsNegative {
            return math.MinInt32
        }
        return math.MaxInt32
    }
    for i := idx-1; i >= lowerLimit; i-- {
        res += numSlice[i] * mult
        // check for overflow
        resInt += int(numSlice[i]) * multInt
        mult *= int32(10)
        multInt *= 10
        if resInt != int(res) {
            if numberIsNegative {
                return math.MinInt32
            }
            return math.MaxInt32
        }
    }
    if numberIsNegative {
        return -int(res)
    }
    return int(res)
}
