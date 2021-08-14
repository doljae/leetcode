from typing import *
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if k == 1:
            return nums

        answer = []
        q = deque([])
        for i, val in enumerate(nums):
            while q and q[0] <= i - k:
                q.popleft()

            while q and nums[q[-1]] <= val:
                q.pop()

            q.append(i)

            if i >= k - 1:
                answer.append(nums[q[0]])

        return answer
