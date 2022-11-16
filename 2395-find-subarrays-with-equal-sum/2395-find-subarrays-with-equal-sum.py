class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        m = defaultdict(int)
        
        for i in range(len(nums)-1):
            m[nums[i] + nums[i+1]] += 1
        
        for key in m:
            if m[key] >= 2:
                return True
        
        return False