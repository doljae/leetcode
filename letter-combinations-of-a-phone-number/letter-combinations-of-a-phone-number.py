from collections import defaultdict
from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        answer = []
        seq = list(digits)
        phone = defaultdict(list)
        alpha = ord("a")
        for num in range(2, 10):
            if num in [7, 9]:
                for i in range(4):
                    phone[num].append(chr(alpha))
                    alpha += 1
            else:
                for i in range(3):
                    phone[num].append(chr(alpha))
                    alpha += 1

        def dfs(index, res):
            if index == len(seq):
                answer.append("".join(res))
                return

            for item in phone[int(seq[index])]:
                dfs(index + 1, res + [item])

        dfs(0, [])
        return answer