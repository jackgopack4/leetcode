/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    // first, traverse list once to determine length
    lenList := 0
    cur := head
    for {
        if cur == nil {
            break
        }
        if cur.Next == nil {
            lenList += 1
            break
        }
        cur = cur.Next
        lenList += 1
    }
    fmt.Println(lenList)
    // then, traverse second time to len(list)-n (1 == end, len(list) == start)
    // modify pointer
    // edge cases: n = len(list) or 1
    if lenList == 1 {
        return nil
    }
    if n == lenList {
        return head.Next
    }
    cur = head
    for i := 1; i < lenList-n; i++ {
        cur = cur.Next
    }
    fmt.Println(cur.Val)
    // if start of list, just need to return pointer to second node
    // if end of list, just need to remove pointer for second-last node
    cur.Next = cur.Next.Next

    return head
}
