class Solution:
    def isThree(self, num: int) -> bool:
        
        cnt = 0
        for i in range(1, num+1):
            if num % i == 0:
                cnt += 1
                
        return cnt == 3