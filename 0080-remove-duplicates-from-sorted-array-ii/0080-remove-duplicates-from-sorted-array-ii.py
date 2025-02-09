class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        target_index = 0
        last_num = -float("inf")
        last_num_cnt = 0

        i = 0
        while i < len(nums):
            num = nums[i]
            if num != last_num:
                last_num_cnt = 0
            nums[target_index] = num
            last_num = num
            target_index += 1
            last_num_cnt += 1
            if last_num_cnt == 2:
                while i + 1 < len(nums) and last_num == nums[i + 1]:
                    i += 1
                last_num_cnt = 0
            i += 1

        return target_index
