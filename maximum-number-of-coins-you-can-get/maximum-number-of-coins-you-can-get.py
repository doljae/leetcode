from typing import *
from collections import deque


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles_q = deque(sorted(piles, reverse=True))
        
        answer = 0
        while piles_q:
            alice, me, bob = piles_q.popleft(), piles_q.popleft(), piles_q.pop()
            answer += me

        return answer
