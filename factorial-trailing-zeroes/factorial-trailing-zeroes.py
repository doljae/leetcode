class Solution:
    def trailingZeroes(self, n: int) -> int:
        answer = 0
        cur = 5
        while cur <= n:
            answer += n // cur
            cur *= 5
        return answer