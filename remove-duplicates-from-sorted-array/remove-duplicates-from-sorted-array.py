from typing import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        saved_val, target_index = nums[0], 1
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                if nums[i] == saved_val:
                    continue
                else:
                    saved_val, nums[target_index] = nums[i], nums[i]
                    target_index += 1
        gap = len(nums) - target_index
        while gap > 0:
            nums.pop()
            gap -= 1
        return len(nums)