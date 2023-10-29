class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        result = 0

        previous_value = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > previous_value:
                k = (nums[i] + previous_value - 1) // previous_value
                result += (k - 1)
                previous_value = nums[i] // k
            else:
                previous_value = nums[i]

        return result