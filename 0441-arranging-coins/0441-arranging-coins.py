class Solution:
    def arrangeCoins(self, n: int) -> int:
        result = 1
        while True:
            temp = result * (result + 1) // 2
            if temp == n:
                return result
            elif temp > n:
                return result - 1
            else:
                result += 1