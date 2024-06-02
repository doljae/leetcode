from copy import deepcopy
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def permutaion(cur, start_index, nums, length):

            if len(cur) == length:
                result.append(deepcopy(cur))
                return

            for i in range(start_index, len(nums)):
                cur.append(nums[i])
                permutaion(cur, i + 1, nums, length)
                cur.pop()

        for i in range(len(nums) + 1):
            permutaion([], 0, nums, i)

        return result