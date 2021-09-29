from typing import *
from collections import defaultdict


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1 = defaultdict(int)

        for index, value in enumerate(numbers):
            if target - value in dict1:
                return [dict1[target - value] + 1, index + 1]
            dict1[value] = index

