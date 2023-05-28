import math


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return math.sqrt(num).is_integer()