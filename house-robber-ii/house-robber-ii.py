class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        first, second = [0] * (len(nums) + 1), [0] * (len(nums) + 1)
        first[1] = nums[0]

        for i in range(2, len(nums) + 1):
            first[i] = max(first[i - 1], first[i - 2] + nums[i - 1])
            second[i] = max(second[i - 1], second[i - 2] + nums[i - 1])

        return max(first[len(nums) - 1], second[len(nums)])
