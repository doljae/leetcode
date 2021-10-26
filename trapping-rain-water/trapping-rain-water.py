from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:
        stack, answer = [], 0

        for i in range(len(height)):
            cur = height[i]
            if not stack or (stack and height[stack[-1]] >= cur):
                stack.append(i)

            else:
                # print(stack)
                while stack and height[stack[-1]]<=cur:
                    target = height[stack[-1]]
                    while stack and height[stack[-1]] == target:
                        stack.pop()
                    if stack:
                        width = i - stack[-1] - 1
                        length = min(cur, height[stack[-1]]) - target
                        answer += width * length
                stack.append(i)
            # print(stack, answer)
        return answer
