class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        
        seq = [0] * 26
        
        for char in s : 
            seq[ord(char) - ord("a")] += 1
        
        for char in t:
            seq[ord(char) - ord("a")] -= 1
        
        for i in range(26):
            if seq[i] < 0 :
                return chr(i + ord("a"))