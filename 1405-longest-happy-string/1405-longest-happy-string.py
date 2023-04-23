import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for count, token in (-a, 'a'), (-b, 'b'), (-c, 'c'):
            if count: heapq.heappush(max_heap, (count, token))
        result = []
        while max_heap:
            count, token = heapq.heappop(max_heap)
            if len(result) > 1 and result[-2] == result[-1] == token:
                if not max_heap: break
                count, token = heapq.heapreplace(max_heap, (count, token))
            result.append(token)
            if count + 1: heapq.heappush(max_heap, (count + 1, token))
        return ''.join(result)