from typing import *


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        list1 = list(s)

        def dfs(pos, seq):
            if pos == len(s):
                answer.append("".join(seq[:]))
                return

            if list1[pos].isalpha():
                dfs(pos + 1, seq+[list1[pos].lower()])
                dfs(pos + 1, seq+[list1[pos].upper()])
            else:
                dfs(pos + 1, seq + [list1[pos]])

        dfs(0, [])
        return answer
