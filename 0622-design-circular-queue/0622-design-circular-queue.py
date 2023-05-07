#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = collections.deque([])
        self.size = k

    def enQueue(self, value: int) -> bool:
        if len(self.q) == self.size:
            return False
        self.q.append(value)
        return True

    def deQueue(self) -> bool:
        if not self.q:
            return False
        self.q.popleft()
        return True

    def Front(self) -> int:
        if not self.q:
            return -1
        return self.q[0]

    def Rear(self) -> int:
        if not self.q:
            return -1
        return self.q[-1]

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.size
