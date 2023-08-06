# 88. Merge Sorted Array

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        cur1 = m-1
        cur2 = n-1
        mergedIndex = m+n-1

        while cur2 >= 0:
            if cur1 >= 0 and nums2[cur2] < nums1[cur1]:
                nums1[mergedIndex] = nums1[cur1]
                cur1-=1
            else:
                nums1[mergedIndex] = nums2[cur2]
                cur2 -= 1
            mergedIndex -=1
