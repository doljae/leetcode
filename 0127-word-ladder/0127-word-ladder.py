from _collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        dictionary = set(wordList)

        if endWord not in dictionary:
            return 0

        result = 1
        q = deque([(beginWord, result)])
        visited = {beginWord}

        while q:
            cur_str, cur_cnt = q.popleft()

            for i in range(len(cur_str)):
                for j in range(ord('a'), ord('z') + 1):
                    temp = cur_str[:i] + chr(j) + cur_str[i + 1:]

                    if temp == endWord:
                        return cur_cnt + 1

                    if temp in dictionary and temp not in visited:
                        q.append((temp, cur_cnt + 1))
                        visited.add(temp)

        return 0