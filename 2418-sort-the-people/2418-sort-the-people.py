class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp = list(zip(names, heights))
        
        temp.sort(key = lambda x: x[1], reverse = True)
        
        return [item[0] for item in temp]