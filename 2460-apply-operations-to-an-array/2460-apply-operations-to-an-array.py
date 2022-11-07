class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        result = []

        for i in range(0, len(nums)):
            if i != len(nums) - 1 and nums[i] == nums[i + 1]:
                nums[i], nums[i + 1] = nums[i] * 2, 0
            if nums[i] != 0:
                result.append(nums[i])

        return result + [0] * (len(nums) - len(result))