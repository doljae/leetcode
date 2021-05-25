class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = []
        for item in matrix:
            temp += item
        return sorted(temp)[k-1]
        