from typing import *


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        height, width = len(rowSum), len(colSum)

        answer = [[0] * width for _ in range(height)]

        i, j = 0, 0
        while i < height and j < width:
            target = min(rowSum[i], colSum[j])

            answer[i][j] = target

            if rowSum[i] == colSum[j]:
                i, j = i + 1, j + 1

            elif rowSum[i] > colSum[j]:
                rowSum[i] -= colSum[j]
                j += 1

            elif rowSum[i] < colSum[j]:
                colSum[j] -= rowSum[i]
                i += 1

        return answer