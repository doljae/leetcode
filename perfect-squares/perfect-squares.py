class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([(n, 0)])
        set1 = {n}
        while q:
            cur_num, cur_level = q.popleft()
            if cur_num == 0:
                return cur_level
            j = 1
            while cur_num >= j * j:
                temp = cur_num - (j * j)
                if temp not in set1:
                    set1.add(temp)
                    q.append((temp, cur_level + 1))
                j += 1