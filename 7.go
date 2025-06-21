import (
    // "math"
    "strconv"
)
func reverse(x int) int {
    xStr := strconv.Itoa(x)
    mult := 1
    if string(xStr[0]) == "-" {
        mult = -1
        xStr = xStr[1:]
    }
    var res int32
    res = 0
    // we need to add the digits back together, then check for overflow.
    // convert to negative by multiplying by "mult" var
    // reasonably confident that will only overflow on last bit
    // ok actually it could happen more
    for i := 0; i < len(xStr); i++ {
        digit, err := strconv.Atoi(string(xStr[i]))
        if err != nil {
            panic("shouldn't happen")
        }
        addedVal := mult * digit
        addedValInt32 := int32(mult * digit)
        resInt := int(res)
        res += addedValInt32
        resInt += addedVal
        if addedVal != int(addedValInt32) || resInt != int(res) {
            return 0
        }
        mult *= 10
    }
    return int(res)
}
