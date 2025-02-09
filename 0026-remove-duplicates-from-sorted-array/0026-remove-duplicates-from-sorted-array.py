class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        target_index = 0
        last_num = nums[0]

        for i, num in enumerate(nums):
            if target_index == 0:
                nums[target_index] = num
                last_num = num
                target_index += 1
            else:
                if num != last_num:
                    nums[target_index] = num
                    last_num = num
                    target_index += 1

        return target_index
