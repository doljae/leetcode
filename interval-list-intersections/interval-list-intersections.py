from typing import *


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []

        p1, p2 = 0, 0
        while p1 < len(firstList) and p2 < len(secondList):
            c1, c2 = firstList[p1], secondList[p2]
            s1, e1 = c1
            s2, e2 = c2

            if e1 < s2:
                p1 += 1
            elif e2 < s1:
                p2 += 1
            else:
                answer.append([max(s1, s2), min(e1, e2)])
                if e1 <= e2:
                    p1 += 1
                else:
                    p2 += 1

        return answer
