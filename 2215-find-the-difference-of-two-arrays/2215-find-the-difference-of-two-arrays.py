class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        map1 = [0]*2002
        map2 = [0]*2002
        
        for num in nums1:
            map1[num+1000]+=1
        
        for num in nums2:
            map2[num+1000]+=1
        
        r1, r2 = [], []
        for i in range(2002):
            if map1[i] and not map2[i]:
                r1.append(i-1000)
            elif not map1[i] and map2[i]:
                r2.append(i-1000)
        
        return [r1,r2]
        
        