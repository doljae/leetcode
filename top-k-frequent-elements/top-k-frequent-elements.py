from typing import *
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = Counter()
        for num in nums:
            counter_dict[num] += 1
        return list(map(lambda x: x[0], counter_dict.most_common(k)))[:k]
