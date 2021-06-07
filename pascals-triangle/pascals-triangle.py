from typing import *


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            answer = [[1], [1, 1]]
            for index in range(2, numRows):
                cur = 0
                temp = []
                while cur < index + 1:
                    if cur in [0, index]:
                        temp.append(1)
                    else:
                        temp.append(answer[index - 1][cur - 1] + answer[index - 1][cur])
                    cur += 1
                answer.append(temp)
            return answer