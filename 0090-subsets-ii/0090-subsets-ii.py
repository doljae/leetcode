from itertools import combinations
from typing import *


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums) + 1):
            for item in combinations(nums, i):
                result.add(tuple(sorted(list(item))))

        return list(map(lambda x: list(x), list(result)))