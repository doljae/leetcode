class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        temp = bin(n)[2:]
        
        a, b = True, True
        a = temp[0]=="1"
        if len(temp)>1:
            b = list(set(list(temp[1:])))[0]=="0" and len(list(set(list(temp[1:])))) == 1
        
        return a and b