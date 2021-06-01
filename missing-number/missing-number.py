class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = len(nums)
        return (target * (target+1)//2) - sum(nums)