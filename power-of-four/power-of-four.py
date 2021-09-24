class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        if 1 < n < 4:
            return False
        if n == 1:
            return True

        cur = 4
        while cur <= n:
            if cur == n:
                return True
            cur *= 4

        return False