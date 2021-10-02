class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        q=deque([])
        set1=set()
        answer=0
        for i in range(len(s)):
            if not q:
                q.append(s[i])
                set1.add(s[i])
            else:
                if s[i] in set1:
                    while q[0]!=s[i]:
                        set1.remove(q.popleft())
                    set1.remove(q.popleft())
                    q.append(s[i])
                    set1.add(s[i])
                else:
                    q.append(s[i])
                    set1.add(s[i])
            
            answer=max(answer,len(q))
        return answer
                