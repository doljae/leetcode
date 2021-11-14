from typing import *


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        answer = 0

        while tickets[k] != 0:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    answer += 1
                    tickets[i] -= 1
                    if tickets[i] == 0 and i == k:
                        break

        return answer
