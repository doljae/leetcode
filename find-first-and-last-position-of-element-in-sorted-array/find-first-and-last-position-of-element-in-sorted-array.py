from typing import *


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1

        t1 = start if nums[start] == target else -1

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1

        t2 = start - 1 if nums[start - 1] == target else -1

        return [t1, t2]
