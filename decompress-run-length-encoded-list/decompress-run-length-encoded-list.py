class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        if not nums:
            return None
        index = 0
        answer =[]
        while index<len(nums):
            freq, val = nums[index], nums[index+1]
            answer += [val]*freq
            index+=2
        return answer