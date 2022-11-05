class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        m = defaultdict(list)
        
        for num in nums:
            m[abs(num)].append(num > 0)
        
        result = -1
        
        for key in m:
            if True in m[key] and False in m[key]:
                result = max(result, key)
        
        return result