class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        visited = [0] * 100001
        
        for num in nums:
            visited[num] += 1
        
        result, max_num = -1, 0
        for index, num in enumerate(visited):
            if index % 2 == 0 and num > max_num:
                result, max_num = index, num
        
        return result