from typing import *
from collections import defaultdict


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1 = defaultdict(list)
        dict2 = defaultdict(list)
        for index, number in enumerate(numbers):
            dict1[target - number].append(index)
            dict2[number].append(index)
        # print(dict1)
        # print(dict2)
        for index, number in enumerate(numbers):
            target_number = target - number

            if number == target_number and len(dict1[target_number]) >= 2:
                return [dict1[target_number][0] + 1, dict1[target_number][1] + 1]

            if target_number in dict2:
                return [index + 1, dict2[target_number][0] + 1]
