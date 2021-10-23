class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        for char in set(list(s)):
            if s.count(char) < k:
                return max(self.longestSubstring(sub_str, k) for sub_str in s.split(char))

        return len(s)
