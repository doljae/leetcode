# parametric search

from typing import *


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)

        while low < high:
            mid = (low + high) // 2
            subarray_sum, size = 0, 1

            for num in nums:
                if subarray_sum + num <= mid:
                    subarray_sum += num
                else:
                    subarray_sum = num
                    size += 1
            if size > k:
                low = mid + 1
            else:
                high = mid
        return high
