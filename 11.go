func maxArea(height []int) int {
    lp, rp := 0, len(height)-1
    vol := 0
    var tmp int
    for {
        if lp >= rp {
            return vol
        }
        tmp = min(height[lp], height[rp])*(rp-lp)
        if tmp > vol {
            vol = tmp
        }
        if height[lp] > height[rp] {
            rp -= 1
        } else if height[lp] < height[rp] {
            lp += 1
        } else {
            prevLeftHeight := height[lp]
            prevRightHeight := height[rp]
            for {
                if height[lp] <= prevLeftHeight {
                    lp += 1
                }
                if height[rp] <= prevRightHeight {
                    rp -= 1
                }
                if height[lp] > prevLeftHeight && height[rp] > prevRightHeight || lp >= rp {
                    break
                }
            }
        }
    }
    return vol
}
