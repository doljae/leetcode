#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = deque([])
        left = k
        for char in num:
            if not result:
                result.append(char)
            else:
                if result[-1] <= char:
                    result.append(char)
                elif result[-1] > char:
                    while left > 0 and result and result[-1] > char:
                        result.pop()
                        left -= 1
                    result.append(char)

        while result and result[0] == "0":
            result.popleft()

        r = "".join(list(result))
        if len(r) == 0 or len(r) <= left:
            return "0"
        return r[:len(r) - left]