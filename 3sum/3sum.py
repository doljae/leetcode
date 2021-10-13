from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if not nums or len(nums) < 3:
            return []

        nums.sort()
        answer = []
        i = 0
        while i < len(nums) - 2:
            start, end = i + 1, len(nums) - 1
            temp = nums[i]
            while start < end:
                temp2 = temp + nums[start] + nums[end]
                if temp2 == 0:
                    answer.append([nums[i], nums[start], nums[end]])
                    # print(answer)
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start, end = start + 1, end - 1

                elif temp2 > 0:
                    end -= 1

                elif temp2 < 0:
                    start += 1

            while i < len(nums) - 3 and nums[i] == nums[i + 1]:
                i += 1
            i += 1

        return answer