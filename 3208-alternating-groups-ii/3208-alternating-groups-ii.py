from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors += colors[:k - 1]
        result = 0
        cnt = 1
        for i in range(1, len(colors)):
            if colors[i] != colors[i - 1]:
                cnt += 1
            else:
                cnt = 1

            if cnt >= k:
                result += 1

        return result