from heapq import *


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heappush(self.max_heap, -num)
            return

        if self.min_heap and num > self.min_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)
        if len(self.max_heap) - len(self.min_heap) > 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) - len(self.max_heap) > 1:
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) != len(self.min_heap):
            return -self.max_heap[0] if len(self.max_heap) > len(self.min_heap) else self.min_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
