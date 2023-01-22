class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        result1, result2 = None, None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                result1 = nums[:i] + nums[i + 1:]
                result2 = nums[:i + 1] + nums[i + 2:]
                break

        if result1 is None or sorted(result1) == result1:
            return True
        if result2 is None or sorted(result2) == result2:
            return True
        return False
