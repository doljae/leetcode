class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in range(len(nums)):
            temp=0
            for num in nums:
                temp += 1 if nums[i]>num else 0
            answer.append(temp)
        return answer