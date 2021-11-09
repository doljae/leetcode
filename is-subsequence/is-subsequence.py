class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        iterator = iter(t)
        for char in s:
            if char not in iterator:
                return False
        return True