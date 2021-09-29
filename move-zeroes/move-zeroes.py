from typing import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_pointer] = nums[i]
                zero_pointer += 1

        for i in range(zero_pointer, len(nums)):
            nums[i] = 0
        