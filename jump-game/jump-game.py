class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if nums[0] == 0 and len(nums) == 1:
            return True
        
        maximum = 0
        for index, num in enumerate(nums):
            if index > maximum:
                return False
            maximum = max(maximum, index + num)
            if maximum >= len(nums) - 1:
                return True
