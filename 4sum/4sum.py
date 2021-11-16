from typing import *


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        # print(nums)
        answer = set()
        for a in range(len(nums) - 2):
            for b in range(a + 1, len(nums) - 2):
                c, d = b + 1, len(nums) - 1

                while c < d:
                    cur = nums[a] + nums[b] + nums[c] + nums[d]

                    if cur == target:
                        answer.add(tuple([nums[a], nums[b], nums[c], nums[d]]))
                        # print(a, b, c, d)
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        c, d = c + 1, d - 1
                    elif cur > target:
                        d -= 1
                    elif cur < target:
                        c += 1

                # while b < len(nums) - 2 and nums[b] == nums[b + 1]:
                #     b += 1
                # print(b)
                # if b > len(nums) - 2:
                #     break
        return list(map(lambda x: list(x), list(answer)))
