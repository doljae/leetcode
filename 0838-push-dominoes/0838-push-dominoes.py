#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        stack, result = [], []
        r_cnt = False

        for domino in dominoes:
            if domino == ".":
                stack.append(domino)
            elif domino == "R":
                if not r_cnt:
                    result += stack
                    r_cnt = True
                else:
                    size = len(stack)
                    result += ["R"] * size
                stack = [domino]
            elif domino == "L":
                if not r_cnt:
                    size = len(stack)
                    result += ["L"] * (size + 1)
                else:
                    size = len(stack) + 1
                    result += ["R"] * (size // 2)
                    if size % 2 != 0:
                        result.append(".")
                    result += ["L"] * (size // 2)
                    r_cnt = False
                stack = []

        if stack and stack[0] == "R":
            stack = ["R"] * len(stack)

        return "".join(result + stack)