from collections import deque, defaultdict
from typing import *


def convert(word: str):
    char_list = list(map(ord, list(word)))
    result = deque([])
    temp = char_list.pop()
    while char_list:
        result.appendleft(temp - char_list[-1])
        temp = char_list.pop()

    return "*".join(list(map(str, list(result))))


class Solution:
    def oddString(self, words: List[str]) -> str:
        result = defaultdict(list)

        for index, word in enumerate(words):
            result[convert(word)].append(index)

        for key in result:
            if len(result[key]) == 1:
                return words[result[key][0]]


print(Solution().oddString(["adc", "wzy", "abc"]))
