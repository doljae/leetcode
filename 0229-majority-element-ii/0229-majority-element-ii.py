from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result = []
        for item in counter:
            if counter[item] > len(nums) / 3:
                result.append(item)

        return result