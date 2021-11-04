class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        
        a, b = nums[0], nums[-1]
        
        def gcd(a, b):
            while a % b != 0 :
                a, b = b, a%b
            
            return b
        
        return gcd(a, b)