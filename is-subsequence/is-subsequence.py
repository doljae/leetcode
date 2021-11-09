class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        for char in s:
            index = t.find(char)
            if index == -1:
                return False

            t = t[index + 1:]

        return True
