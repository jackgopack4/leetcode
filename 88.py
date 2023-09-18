class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # start from back of nums1, either move n1 or insert n2
        # starting length of nums1 actually m+n
        n1 = m-1
        n2 = n-1
        new_index = m+n-1
        
        while nums2:
            if n1 >= 0 and nums2[-1] < nums1[n1]:
                nums1[new_index] = nums1[n1]
                n1 -= 1
            else:
                nums1[new_index] = nums2[-1]
                nums2.pop()
            new_index -= 1
