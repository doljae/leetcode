class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total, cnt = 0, 0
        
        for num in nums:
            if num % 6 == 0:
                total += num
                cnt += 1
        
        if total == 0:
            return 0
        
        return total // cnt