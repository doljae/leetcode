class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        cur = 0
        while True:
            temp=pow(3,cur)
            if temp>n:
                return False
            if temp==n:
                return True
            cur+=1