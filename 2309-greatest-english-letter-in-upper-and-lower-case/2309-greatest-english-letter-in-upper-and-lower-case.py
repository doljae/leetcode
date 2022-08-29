class Solution:
    def greatestLetter(self, s: str) -> str:
        flag1 = [0] * 26
        flag2 = [0] * 26
        for char in s:
            if char.isupper() is True:
                flag1[ord(char)-ord("A")] +=1
            else:
                flag2[ord(char)-ord("a")] +=1
        for i in range(25, -1, -1):
            if flag1[i] > 0 and flag2[i] > 0:
                return chr(ord("A")+i)
        
        return ""