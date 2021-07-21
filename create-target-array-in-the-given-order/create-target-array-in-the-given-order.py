class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            indexx = index[i]
            num = nums[i]
            answer = answer[:indexx] + [num] + answer[indexx:]
        return answer
        