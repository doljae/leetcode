from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                red += 1
            elif nums[i] == 1:
                white += 1
            else:
                blue += 1

        for i in range(len(nums)):
            if red:
                nums[i] = 0
                red -= 1
            elif white:
                nums[i] = 1
                white -= 1
            else:
                nums[i] = 2
                blue -= 1