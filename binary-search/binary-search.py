from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            temp = nums[mid]

            if temp <= target:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1 if target == nums[left - 1] else -1