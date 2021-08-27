from typing import *
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        answer = [0] * len(sorted_deck)
        q = deque([i for i in range(len(sorted_deck))])

        for i in range(len(sorted_deck)):
            answer[q.popleft()] = sorted_deck[i]
            if q:
                q.append(q.popleft())

        return answer