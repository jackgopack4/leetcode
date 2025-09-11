/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
import (
    "math"
)

var maxPathSeen int

func maxPathSum(root *TreeNode) int {
    maxPathSeen = math.MinInt
    _ = maxPathSumRecurse(root)
    return maxPathSeen
}

func maxPathSumRecurse(root *TreeNode) int {
    if root == nil {
        return 0
    }
    maxLeft := max(0, maxPathSumRecurse(root.Left))
    maxRight := max(0, maxPathSumRecurse(root.Right))
    // mu.RLock()
    // defer mu.Unlock()
    maxPathSeen = max(maxPathSeen, maxLeft+maxRight+root.Val)
    fmt.Println(maxPathSeen)
    return max(root.Val + maxLeft, root.Val + maxRight)
}
