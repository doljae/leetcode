class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n:
            n = n & (n - 1)
            answer += 1
        return answer
