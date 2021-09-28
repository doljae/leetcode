class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            temp = nums[mid]
            if temp == target:
                return mid
            elif temp <= target:
                left = mid + 1
            else:
                right = mid - 1

        return left
