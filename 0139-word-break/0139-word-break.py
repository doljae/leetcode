from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        while s:
            flag = False
            for word in wordDict:
                if word in s:
                    s = s.replace(word, "")
                    flag = True
                    break

            if not flag:
                return False
        
        return True
