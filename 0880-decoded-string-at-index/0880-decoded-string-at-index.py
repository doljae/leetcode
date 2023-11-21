class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_len = 0
        for char in s:
            if char.isalpha():
                decoded_len += 1
            else:
                decoded_len *= int(char)

        for i in range(len(s) - 1, -1, -1):
            cur_char = s[i]
            if cur_char.isdigit():
                decoded_len //= int(cur_char)
                k %= decoded_len
            else:
                if k == 0 or decoded_len == k:
                    return cur_char
                decoded_len -= 1

        return ""