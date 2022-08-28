from itertools import combinations

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = [0]
        for n in nums:
            prefix_sum.append(prefix_sum[-1] + n)
        ans = []    
        for q in queries:
            ans.append(bisect.bisect(prefix_sum, q) - 1)
        return ans