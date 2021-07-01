from typing import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        MAX_VAL = pow(10, 9)
        MIN_VAL = -MAX_VAL
        if not nums:
            return 0
        set1 = set()
        for num in nums:
            set1.add(num)
        checked = set()
        answer = 0
        for num in nums:
            cur = num
            if cur not in checked:
                temp = 1
                checked.add(cur)
                cur2 = cur
                while cur2 + 1 in set1:
                    temp += 1
                    cur2 += 1
                    checked.add(cur2)
                cur2 = cur
                while cur2 - 1 in set1:
                    temp += 1
                    cur2 -= 1
                    checked.add(cur2)
                answer = max(answer, temp)
        return answer