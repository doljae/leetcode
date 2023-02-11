import math
from typing import *


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        # first, third, second
        third = -math.inf
        second = []
        for i in range(len(nums) - 1, -1, -1):
            first = nums[i]
            if first < third:
                return True

            while second and nums[i] > second[-1]:
                third = second.pop()

            second.append(nums[i])
        return False
