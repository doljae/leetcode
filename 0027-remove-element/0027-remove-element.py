class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        while i != len(nums):
            cur = nums[i]
            if cur == val:
                del nums[i]
            else:
                i += 1

        return len(nums)