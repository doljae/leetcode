class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cur = nums[0]
        
        for i in range(1, len(nums)):
            cur ^= nums[i]
        
        return cur