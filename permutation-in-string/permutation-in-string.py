class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_cnt, s2_cnt = [0] * 26, [0] * 26
        for char in s1:
            s1_cnt[ord(char) - ord('a')] += 1

        for i in range(len(s2)):
            s2_cnt[ord(s2[i]) - ord('a')] += 1

            if i >= len(s1):
                s2_cnt[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if s1_cnt == s2_cnt:
                return True

        return False
