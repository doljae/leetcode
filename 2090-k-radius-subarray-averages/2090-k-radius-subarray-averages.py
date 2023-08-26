from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = 0
        right_window_flag = False
        for i in range(len(nums)):
            if i < k:
                window += nums[i]
                result.append(-1)
            elif i + k > len(nums) - 1:
                result.append(-1)
            else:
                if not right_window_flag:
                    window += sum(nums[i:i + 1 + k])
                    right_window_flag = True
                else:
                    window -= nums[i - k - 1]
                    window += nums[i + k]
                # print(f"{nums[i]} {window}")
                result.append(window // (k * 2 + 1))

        return result