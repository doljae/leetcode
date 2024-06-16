class Solution(object):
    def longestPalindrome(self, s):
        res=""
        for i in range(len(s)):
            res=max(self.solution(s,i,i),
                   self.solution(s,i,i+1),
                   res, key=len)
        return res
    
    
    def solution(self,s,start,end):
        while 0<=start and end<len(s):
            if s[start]==s[end]:
                start,end = start-1, end+1
            else:
                break
        return s[start+1:end]