/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    // edge cases - both lists 0, list1 0, list2 0
    // else, set list1 to be lower, mark head
    // then, iterate through, if l1ptr.Val <= l2ptr.Val, iterate, else merge
    if list1 == nil {
        return list2
    }
    if list2 == nil {
        return list1
    }
    if list1.Val > list2.Val {
        list1, list2 = list2, list1
    }
    cur := &ListNode{
        Val: list1.Val,
    }
    head := cur
    list1 = list1.Next
    l1ptr, l2ptr := list1, list2
    for {
        if l1ptr == nil || l2ptr == nil {
            break
        }
        if l1ptr.Val <= l2ptr.Val {
            cur.Next = l1ptr
            l1ptr = l1ptr.Next
        } else {
            cur.Next = l2ptr
            l2ptr = l2ptr.Next
        }
        cur = cur.Next
    }
    if l1ptr != nil {
        cur.Next = l1ptr
    } else {
        cur.Next = l2ptr
    }
    return head
}
