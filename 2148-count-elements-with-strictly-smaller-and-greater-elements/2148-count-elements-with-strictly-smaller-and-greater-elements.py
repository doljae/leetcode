from sortedcontainers import SortedDict

class Solution:
    def countElements(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if min(nums) < num < max(nums):
                result += 1
        
        return result