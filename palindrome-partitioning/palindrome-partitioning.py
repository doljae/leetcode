from typing import *


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answers = []

        dp = [[0] * (len(s) + 1) for _ in range(len(s))]

        if len(s) == 1:
            return [[s]]
        if len(s) == 2:
            if s[0] == s[1]:
                return [[s], [s[0], s[1]]]
        for i in range(len(dp)):
            dp[i][1] = 1
        for i in range(len(dp) - 1):
            dp[i][2] = 1 if s[i] == s[i + 1] else 0

        for length in range(3, len(s) + 1):
            for index in range(len(s) - length + 1):
                print(index, length)
                if s[index] == s[index + length - 1] and dp[index + 1][length - 2]:
                    dp[index][length] = 1
        # for item in dp:
        #     print(item)

        def dfs(index, seq):
            if index >= len(s):
                if index == len(s):
                    answers.append(seq[:])
                return
            else:
                for i in range(1, len(s) + 1):
                    if dp[index][i]:
                        seq.append(s[index:index + i])
                        dfs(index + i, seq)
                        seq.pop()

        dfs(0, [])
        return answers

