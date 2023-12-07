import collections
from collections import *
from typing import *


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        board = defaultdict(int)

        for char in chars:
            board[char] += 1

        result = ""
        for word in words:
            counter = collections.Counter(word)
            flag = True
            for key in counter:
                if counter[key] > board[key]:
                    flag = False
                    break
            if flag:
                result += word

        return len(result)