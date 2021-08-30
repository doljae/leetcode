from typing import *


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def convert(word):
            index = 0
            check, answer = {}, []
            for char in word:
                if char not in check:
                    check[char] = index
                    index += 1
                answer.append(check[char])

            return answer

        result = []
        converted_pattern = convert(pattern)
        for word in words:
            if convert(word) == converted_pattern:
                result.append(word)

        return result
