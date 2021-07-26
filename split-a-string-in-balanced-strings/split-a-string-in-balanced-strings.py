class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_cnt, l_cnt=0,0
        answer=0
        for char in s:
            if char=="R":
                r_cnt+=1
            else:
                l_cnt+=1
            
            if r_cnt==l_cnt:
                answer+=1
                r_cnt,l_cnt=0,0
        return answer