from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] <= nums[end]:
                end = mid
            else:
                start = mid + 1
        gap = start
        print(gap)
        start, end = 0, len(nums) - 1

        while start <= end:

            mid = (start + end) // 2
            r_mid = (mid + gap) % len(nums)
            if nums[r_mid] == target:
                return r_mid
            elif nums[r_mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1
