from typing import *


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, answer = 0, len(nums) + 1
        cur = 0
        for right in range(len(nums)):
            cur += nums[right]

            while target <= cur:
                answer = min(answer, right - left + 1)
                cur -= nums[left]
                left += 1
        return answer if answer<=len(nums) else 0
