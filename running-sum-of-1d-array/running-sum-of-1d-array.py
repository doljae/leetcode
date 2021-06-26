class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answers=[]
        for i in range(len(nums)):
            if i==0:
                answers.append(nums[i])
            else:
                answers.append(answers[-1]+nums[i])
        return answers