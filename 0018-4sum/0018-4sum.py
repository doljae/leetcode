class Solution:
    def __init__(self):
        self.result = []

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.n_sum(nums, target, 4, [])

        return self.result

    def n_sum(self, nums, target, n, result):
        if len(nums) < n:
            return
        if n < 2:
            return
        if target < nums[0] * n:
            return
        if target > nums[-1] * n:
            return

        if n == 2:
            left, right = 0, len(nums) - 1
            while left < right:
                temp = nums[left] + nums[right]
                if temp == target:
                    self.result.append(result + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif temp < target:
                    left += 1
                elif temp > target:
                    right -= 1
        else:
            for i in range(len(nums) - n + 1):
                if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                    self.n_sum(nums[i + 1:], target - nums[i], n - 1, result + [nums[i]])