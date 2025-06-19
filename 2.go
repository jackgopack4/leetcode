/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var cur1, cur2 int
    res := &ListNode{
        Val: 0,
    }
    tmpPointer := res
    overflow := false
    for {
        if l1 == nil && l2 == nil {
            if overflow {
                tmpPointer.Val = 1
            }
            return res
        }
        if l1 != nil {
            cur1 = l1.Val
        } else {
            cur1 = 0
        }
        if l2 != nil {
            cur2  = l2.Val
        } else {
            cur2 = 0
        }

        var tmp int
        tmp, overflow = bitAdder(cur1, cur2, overflow)
        tmpPointer.Val = tmp

        if l1 != nil{
            l1 = l1.Next
        }
        if l2 != nil {
            l2 = l2.Next
        }
        if overflow || (l1 != nil) || (l2 != nil) {
            tmpPointer.Next = &ListNode{
                Val: 0,
            }
            tmpPointer = tmpPointer.Next
        } else {
            break
        }
    }
    return res
}

func bitAdder(b1, b2 int, bit bool) (sum int, overflow bool) {
    sum = b1+b2
    if bit {
        sum += 1
    }
    if sum > 9 {
        overflow = true
        sum -= 10
    }
    return
}
