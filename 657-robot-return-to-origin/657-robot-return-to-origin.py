class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dir_map = {"R":(0,1),"L":(0,-1),"U":(-1,0),"D":(1,0)}
        
        x, y = 0, 0
        for move in moves:
            x, y = x + dir_map[move][0], y + dir_map[move][1]
        
        return x == y == 0