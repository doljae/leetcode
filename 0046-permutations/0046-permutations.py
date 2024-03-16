from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permutation(nums, [], result)

        return result

    def permutation(self, nums, cur, result):
        if len(cur) == len(nums):
            result.append(cur.copy())
            return

        for i in range(len(nums)):
            temp = nums[i]
            if temp != -20:
                cur.append(temp)
                nums[i] = -20
                self.permutation(nums, cur, result)
                nums[i] = temp
                cur.pop()
