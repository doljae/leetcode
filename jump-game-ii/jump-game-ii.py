from typing import *


class Solution:
    def jump(self, nums: List[int]) -> int:
        start, end, cnt = 0, 0, 0

        while end < len(nums) - 1:
            cnt += 1
            max_end = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= len(nums) - 1:
                    return cnt
                max_end = max(max_end, i + nums[i])

            start, end = end + 1, max_end
        return cnt
