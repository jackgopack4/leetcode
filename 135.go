// Idea - pass through each increasing rightpointer, then when decrease move leftpointer to local 
// max. Continue issuing candies (including negative) until we start to go back up again. 
// Normalize each block, then move left pointer to that first increased one
func candy(ratings []int) int {
    lp, rp := 0, 1
    leftCandies := make([]int, len(ratings), len(ratings))
    rightCandies := make([]int, len(ratings), len(ratings))
    for i := range leftCandies {
        leftCandies[i] = 1
    }
    for {
        if rp >= len(ratings) {
            break
        }
        if ratings[lp] < ratings[rp] {
            leftCandies[rp] = leftCandies[lp] + 1
        } /*else if ratings[lp] == ratings[rp] {
            leftCandies[rp] = leftCandies[lp]
        }*/
        // don't need to set 1 since we did at top
        rp += 1
        lp += 1
    }
    for i := range rightCandies {
        rightCandies[i] = 1
    }
    rp = len(ratings)-1
    lp = len(ratings)-2
    for {
        if lp < 0 {
            break
        }
        if ratings[rp] < ratings[lp] {
            rightCandies[lp] = rightCandies[rp] + 1
        } /*else if ratings[rp] == ratings[lp] {
            rightCandies[lp] = rightCandies[rp]
        }*/
        rp -= 1
        lp -= 1
    }
    totalCandies := 0
    for i := 0; i< len(ratings); i++ {
        totalCandies += max(leftCandies[i],rightCandies[i])
    }
    return totalCandies
  
