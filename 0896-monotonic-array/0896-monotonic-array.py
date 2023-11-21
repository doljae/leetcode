from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_asc = None
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i] > nums[i + 1]:
                if is_asc is None:
                    is_asc = False
                elif is_asc is True:
                    return False
            elif nums[i] < nums[i + 1]:
                if is_asc is None:
                    is_asc = True
                elif is_asc is False:
                    return False

        return True