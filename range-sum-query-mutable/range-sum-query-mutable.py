from typing import *


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0] + nums
        self.tree = [0] * (len(nums) + 1)
        for i in range(1, len(self.nums)):
            # print(i,self.nums[i])
            self.update_init(i, self.nums[i])
            # print(self.tree)
        # print(self.tree)

    def update_init(self, index, value):
        while index <= len(self.tree) - 1:
            # print(index)
            self.tree[index] += value
            index += index & -index

    def update(self, index: int, val: int) -> None:
        index += 1
        gap = val - self.nums[index]
        self.update_init(index, gap)
        self.nums[index]=val
        # print(self.tree)

    def sumRange(self, left: int, right: int) -> int:
        left_sum = 0
        while left >= 1:
            left_sum += self.tree[left]
            left -= left & -left
        right += 1
        right_sum = 0
        while right >= 1:
            right_sum += self.tree[right]
            right -= right & -right
        return right_sum - left_sum
