class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        row,col={},{}
        for i, item in enumerate(grid):
            row[i]=max(item)
        
        for i, item in enumerate(list(zip(*grid))):
            col[i]=max(item)
        
        answer=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                answer+=(min(row[i],col[j])-grid[i][j])
        return answer
        