from typing import *


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seq = [0] * (len(nums) + 2)
        max_len = len(seq)
        for num in nums:
            if 0 < num < max_len:
                seq[num] = 1

        for i in range(1, len(seq)):
            if seq[i] == 0:
                return i
