from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        remove_index = [0] * len(nums)
        for index, num in enumerate(nums):
            if num == val:
                remove_index[index] = 1

        for index, num in enumerate(nums):
            if remove_index[index] == 1:
                nums[index] = -1

        nums.sort(reverse=True)
        while nums and nums[-1] == -1:
            nums.pop()

        return len(nums)
