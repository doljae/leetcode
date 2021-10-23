from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        most_uncommon_char, cnt = Counter(s).most_common()[-1]
        if cnt < k:
            return max(self.longestSubstring(t, k) for t in s.split(most_uncommon_char))

        return len(s)
