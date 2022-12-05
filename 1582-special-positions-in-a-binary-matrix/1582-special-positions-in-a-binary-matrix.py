class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sum = [0] * len(mat)
        col_sum = [0] * len(mat[0])
        
        for i in range(len(row_sum)):
            row_sum[i] = sum(mat[i])
        
        zipped = list(zip(*mat))
        for i in range(len(col_sum)):
            col_sum[i] = sum(zipped[i])
            
        result = 0 
        for i in range(len(row_sum)):
            for j in range(len(col_sum)):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    result += 1
        
        return result
                    