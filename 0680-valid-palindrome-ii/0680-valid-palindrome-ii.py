class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                candi1 = s[:left] + s[left + 1:]
                candi2 = s[:right] + s[right + 1:]

                if candi1 == candi1[::-1] or candi2 == candi2[::-1]:
                    return True
                else:
                    return False

        return True
