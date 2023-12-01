class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return list(sorted(nums, key = lambda x:x%2))