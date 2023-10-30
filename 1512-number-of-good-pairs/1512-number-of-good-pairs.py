from itertools import combinations
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for item in combinations(nums, 2):
            a, b = item
            if a == b:
                result += 1

        return result
