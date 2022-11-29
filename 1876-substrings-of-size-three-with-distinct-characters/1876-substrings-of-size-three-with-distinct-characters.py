class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)-2):
            temp = list(s[i:i+3])
            if len(set(temp)) == 3:
                result += 1
        
        return result
                
            