from typing import *


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []

        for index, row in enumerate(triangle):
            temp = []
            for index2, value in enumerate(row):
                if index == 0:
                    answer = value
                else:
                    if index2 == 0:
                        answer = dp[index - 1][0] + value
                    elif index2 == len(row) - 1:
                        answer = dp[index - 1][-1] + value
                    else:
                        answer = min(dp[index - 1][index2 - 1], dp[index - 1][index2]) + value

                temp.append(answer)
            dp.append(temp[:])

        return min(dp[-1])