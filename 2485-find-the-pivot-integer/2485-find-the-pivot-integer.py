class Solution:
    def pivotInteger(self, n: int) -> int:
        
        for i in range(n, 0, -1):
            
            left = i*(i+1) // 2
            right = n*(n+1) // 2 - left + i
            
            if left == right:
                return i
        
        return -1