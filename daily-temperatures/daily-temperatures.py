from typing import *

from collections import deque


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        index = [i for i in range(len(T))]
        new_list = list(map(lambda x, y: (x, y), index, T))
        stack, answer = [], []
        while new_list:
            cur = new_list.pop()
            # print(stack, cur)
            if not answer:
                answer.append(0)
                stack.append(cur)
            else:
                while stack and stack[-1][1] <= cur[1]:
                    stack.pop()
                if not stack:
                    answer.append(0)
                    stack.append(cur)
                else:
                    answer.append(stack[-1][0] - cur[0])
                    stack.append(cur)
            # print(answer)
            # print()
        return answer[::-1]
