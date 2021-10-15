from typing import *


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, prod = 0, 1
        answer = 0
        for right in range(len(nums)):
            prod *= nums[right]

            while left <= right and prod >= k:
                prod /= nums[left]
                left += 1
            answer += (right - left + 1)
        return answer
