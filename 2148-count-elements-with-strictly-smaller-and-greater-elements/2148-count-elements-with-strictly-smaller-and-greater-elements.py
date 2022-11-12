class Solution:
    def countElements(self, nums: List[int]) -> int:
        result = 0
        nums = sorted(nums)
        
        check = [0] * 200002
        cnt = [0] * 200002
        
        for num in nums:
            check[num + 100000] = 1
        
        prefix_sum = [check[0]]
        
        for i in range(1, len(check)):
            prefix_sum.append(prefix_sum[-1] + check[i])
        
        for num in nums:
            if 1 <= prefix_sum[num  + 99999] < prefix_sum[num + 100000] < prefix_sum[-1]:
                result += check[num + 100000]
        
        return result
            
        