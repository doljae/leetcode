from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a, b = Counter(word1), Counter(word2)
        return sorted(a.values()) == sorted(b.values()) and sorted(a.keys()) == sorted(b.keys())
