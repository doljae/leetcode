from typing import *
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
            else:
                target_index = bisect_left(stack, num)
                if target_index == len(stack):
                    stack.append(num)
                else:
                    stack[target_index] = num
        print(stack)
        return len(stack)
