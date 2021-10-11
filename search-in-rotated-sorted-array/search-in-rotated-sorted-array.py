from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        new_nums = nums + nums
        prev = -float("inf")
        gap = 0
        for index, num in enumerate(new_nums):
            if num < prev:
                gap = index
                break
            prev = num

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2

            if new_nums[gap:][mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        # print(start)
        if start >= len(nums) or new_nums[gap:][start] != target:
            return -1
        return (start + gap) % len(nums)
