from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque([])
        visited = set()
        result = 0
        for char in s:
            if not q:
                q.append(char)
                visited.add(char)
            else:
                if char not in visited:
                    q.append(char)
                    visited.add(char)
                else:
                    while q and q[0] != char:
                        visited.remove(q.popleft())
                    visited.remove(q.popleft())
                    q.append(char)
                    visited.add(char)
                    
            result = max(result, len(q))

        return result