from _collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        dictionary = set(wordList)

        if endWord not in dictionary:
            return 0

        q = deque([beginWord])
        visited = {beginWord}
        result = 1

        while q:
            for index in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return result

                for i in range(len(cur)):
                    for j in range(ord('a'), ord('z') + 1):
                        temp = cur[:i] + chr(j) + cur[i + 1:]

                        if temp in dictionary and temp not in visited:
                            q.append(temp)
                            visited.add(temp)

            result += 1

        return 0