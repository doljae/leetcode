from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]

        for i in range(1, len(nums)):
            result.append(result[-1] * nums[i - 1])
            
        temp = 1
        for i in range(len(result) - 1, -1, -1):
            result[i] = result[i] * temp
            temp *= nums[i]

        return result
