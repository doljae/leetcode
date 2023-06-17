#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
from typing import *


def up(num, pos):
    temp = list(map(int, list(num)))
    temp[pos] = (temp[pos] + 1) % 10
    return "".join(list(map(str, temp)))


def down(num, pos):
    temp = list(map(int, list(num)))
    temp[pos] = (temp[pos] - 1) % 10
    return "".join(list(map(str, temp)))


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)

        if "0000" in visited:
            return -1

        start = "0000"
        q = deque([(start, 0)])

        while q:
            cur_num, cur_cnt = q.popleft()
            if cur_num == target:
                return cur_cnt

            for i in range(4):
                r1 = up(cur_num, i)
                if r1 not in visited:
                    visited.add(r1)
                    q.append((r1, cur_cnt + 1))
                r2 = down(cur_num, i)
                if r2 not in visited:
                    visited.add(r2)
                    q.append((r2, cur_cnt + 1))

        return -1
