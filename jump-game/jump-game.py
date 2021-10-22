class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maximum=0
        for index, num in enumerate(nums[:len(nums)-1]):
            if index > maximum:
                return False
            maximum = max(maximum, index + num)
        
        return maximum>=len(nums)-1