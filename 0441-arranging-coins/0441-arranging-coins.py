class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (left + right) // 2
            temp = k * (k + 1) // 2
            if temp == n:
                return k
            elif n < temp:
                right = k - 1
            else:
                left = k + 1
        
        return right
