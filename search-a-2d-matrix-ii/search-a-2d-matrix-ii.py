class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp = []
        for item in matrix:
            temp += item
        if target in temp:
            return True
        return False