class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        
        if len(arr) == 2:
            return True
        
        gap = -1
        for i in range(1, len(arr)):
            if gap == -1:
                gap = arr[i] - arr[i-1]
            else:
                if gap != arr[i] - arr[i-1]:
                    return False
        
        return True