from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        for length in range(len(nums)+1):
            for item in combinations(nums, length):
                answer.append(list(item))
        return answer