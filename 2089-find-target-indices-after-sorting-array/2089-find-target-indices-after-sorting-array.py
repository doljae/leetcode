from collections import defaultdict
from typing import *


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        for index, num in enumerate(sorted(nums)):
            d[num].append(index)

        return d[target]
