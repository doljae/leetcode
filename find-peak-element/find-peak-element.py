from typing import *


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return 0
        nums.append(-float("inf"))
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1