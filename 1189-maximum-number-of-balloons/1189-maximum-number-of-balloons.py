#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        board = [0] * 26
        for char in list(text):
            board[ord(char) - ord("a")] += 1

        target_chars = list("balloon")

        result = 0
        while True:
            can_make = True
            for char in target_chars:
                temp = board[ord(char) - ord("a")]
                if temp <= 0:
                    can_make = False
                    break
                board[ord(char) - ord("a")] -= 1
            if can_make:
                result += 1
            else:
                break

        return result