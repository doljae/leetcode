from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        result = -1

        for index, height in enumerate(heights + [0]):
            if not stack:
                stack.append(index)
                result = max(result, height)
            else:
                while stack and heights[stack[-1]] >= height:
                    h = heights[stack.pop()]
                    w = index if not stack else index - stack[-1] - 1
                    result = max(result, h * w)
                stack.append(index)

        return result