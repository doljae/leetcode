class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        erase_flag = False

        while left < right:

            char1, char2 = s[left], s[right]

            if char1 != char2:
                candi1, candi2 = s[left:right], s[left + 1:right + 1]
                return candi1 == candi1[::-1] or candi2 == candi2[::-1]
            left, right = left + 1, right - 1
        return True
