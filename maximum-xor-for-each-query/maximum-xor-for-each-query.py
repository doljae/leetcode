from functools import reduce
from typing import *


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer = []
        target = None
        
        maximum_xor = (1 << maximumBit) - 1
        for i in range(len(nums)):
            if target is None:
                target = reduce(lambda x, y: x ^ y, nums[:len(nums) - i])
            else:
                target ^= nums[len(nums) - i]
            answer.append(maximum_xor ^ target)

        return answer