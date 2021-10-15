from typing import *


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_seq = [0] * 26
        p_seq = [0] * 26
        answer = []
        for char in p:
            p_seq[ord(char) - ord("a")] += 1

        for i, char in enumerate(s):
            s_seq[ord(char) - ord("a")] += 1

            if i >= len(p):
                s_seq[ord(s[i - len(p)]) - ord("a")] -= 1

            if s_seq == p_seq:
                answer.append(i - (len(p) - 1))
        return answer