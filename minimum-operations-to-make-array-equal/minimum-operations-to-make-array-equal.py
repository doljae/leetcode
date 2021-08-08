class Solution:
    def minOperations(self, n: int) -> int:
        answer = 0

        for i in range(1, n, 2):
            answer += (n - i)

        return answer
