class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                answer += 1 if nums[i] == nums[j] else 0
        return answer
        