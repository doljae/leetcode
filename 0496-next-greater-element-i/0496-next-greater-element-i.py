from typing import *


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = []

        for num in nums1:
            if nums2.index(num) == len(nums2):
                ans.append(-1)
            else:
                flag = False
                for temp in nums2[nums2.index(num):]:
                    if temp > num:
                        ans.append(temp)
                        flag = True
                        break
                if not flag:
                    ans.append(-1)

        return ans
