class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            answer = haystack.index(needle)
            return answer
        except:
            return -1