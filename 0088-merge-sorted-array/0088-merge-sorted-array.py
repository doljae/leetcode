class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        p1, p2 = 0, 0
        
        while p1 < m and p2 < n:
            left, right = nums1[p1], nums2[p2]
            if left <= right:
                result.append(left)
                p1 += 1
            else:
                result.append(right)
                p2 += 1
        
        if p1 == m:
            for i in range(p2, n):
                result.append(nums2[i])
        
        if p2 == n:
            for i in range(p1, m):
                result.append(nums1[i])


        for i in range(len(nums1)):
            nums1[i] = result[i]
        

