class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        cur_num = -1000000
        cur_cnt = 0
        write_index = 0
        for i in range(len(nums)):
            if cur_num != nums[i]:
                cur_num = nums[i]
                cur_cnt = 1
                nums[write_index] = cur_num
                write_index += 1
            else:
                cur_cnt += 1
                if cur_cnt > 2:
                    pass
                else:
                    nums[write_index] = cur_num
                    write_index += 1
        for i in range(write_index, len(nums)):
            nums.pop()
        
        return len(nums)

        
            
