class Solution:
    def countPoints(self, rings: str) -> int:
        
        char_list = deque(list(rings))
        
        m = defaultdict(list)
        
        while char_list:
            color, index = char_list.popleft(), int(char_list.popleft())
            
            m[index].append(color)
        
        result = 0 
        target = set(["B", "G", "R"])
        for key in m:
            if set(m[key]) == target:
                result += 1
        
        return result
        