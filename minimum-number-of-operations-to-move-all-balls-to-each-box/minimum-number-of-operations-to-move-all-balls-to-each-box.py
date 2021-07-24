from typing import *


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # brute force
        answer = []
        box_list = list(map(int, list(boxes)))

        for i in range(len(box_list)):
            temp = 0
            for j in range(len(box_list)):
                if i != j and box_list[j] == 1:
                    temp += abs(i - j)
            answer.append(temp)

        return answer
