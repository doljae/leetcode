from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        answer = 0
        while left < right:
            gap = right - left
            length = min(height[left], height[right])
            answer = max(answer, gap * length)
            if length == height[left]:
                left += 1
            else:
                right -= 1
        return answer