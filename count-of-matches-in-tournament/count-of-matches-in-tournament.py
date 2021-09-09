class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        answer = 0
        cur = n
        
        while cur != 1:
            answer += cur // 2
            cur -= cur // 2
        
        return answer