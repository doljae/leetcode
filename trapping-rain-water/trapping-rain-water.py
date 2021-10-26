from typing import *


class Solution:
    def trap(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]
        answer = 0
        while left < right:
            left_max = max(left_max, heights[left])
            right_max = max(right_max, heights[right])

            if left_max <= right_max:
                answer += (left_max - heights[left])
                left += 1
            else:
                answer += (right_max - heights[right])
                right -= 1

        return answer
