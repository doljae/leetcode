from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        a = 0
        while a < len(nums) - 2:
            b, c = a + 1, len(nums) - 1
            while b < c:
                temp = nums[a] + nums[b] + nums[c]
                if temp == 0:
                    result.add((nums[a], nums[b], nums[c]))
                    while b < len(nums) - 1 and nums[b] == nums[b + 1]:
                        b += 1
                    b += 1
                    while c > b and nums[c] == nums[c - 1]:
                        c -= 1
                    c -= 1
                elif temp > 0:
                    c -= 1
                elif temp < 0:
                    b += 1
            while a < len(nums) - 2 and nums[a] == nums[a + 1]:
                a += 1
            a += 1

        return list(map(lambda x: list(x), list(result)))
