class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp=[[0,0] for i in range(n+1)]
        
        dp[0][1] = 1
        dp[1][0] = 1
        dp[1][1] = 0
        
        for i in range(2, n+1):
            dp[i][0] = sum(dp[i-1])
            dp[i][1] = sum(dp[i-2])
        
        return sum(dp[-1])