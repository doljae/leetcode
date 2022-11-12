from sortedcontainers import SortedDict

class Solution:
    def countElements(self, nums: List[int]) -> int:
        sd = SortedDict()
        result = 0
        for num in nums:
            if num in sd:
                sd[num] += 1
            else:
                sd[num] = 1
        
        keys = sd.keys()
        for i in range(1, len(keys)-1):
            if keys[i-1] < keys[i] < keys[i+1]:
                result += sd[keys[i]]
        
        return result
        