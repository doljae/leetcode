from typing import *


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        board = [0] * 26

        for letter in letters:
            board[ord(letter) - ord('a')] = 1

        for i in range(ord(target) - ord('a') + 1, len(board)):
            if board[i]:
                return chr(i + ord('a'))

        return letters[0]