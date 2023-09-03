from typing import *


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        if not nums:
            return []

        while nums:
            cur_num = nums.pop()
            temp_list = [cur_num]
            while nums and nums[-1] == cur_num - 1:
                temp_num = nums.pop()
                temp_list.append(temp_num)
                cur_num = temp_num

            if len(temp_list) == 1:
                result.append(f"{cur_num}")
            else:
                result.append(f"{temp_list[-1]}->{temp_list[0]}")

        return result[::-1]
