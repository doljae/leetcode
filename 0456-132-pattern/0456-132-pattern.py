import math
from typing import *


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        # first, third, second
        third = -math.inf
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            first = nums[i]
            if first < third:
                return True

            while stack and nums[i] > stack[-1]:
                third = stack.pop()

            stack.append(nums[i])
        return False