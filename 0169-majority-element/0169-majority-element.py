class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        result = float("inf")
        for num in nums:
            if result == float("inf"):
                result, cnt = num, 1
            else:
                if result == num:
                    cnt += 1
                else:
                    cnt -= 1
                    if cnt < 0:
                        result = num
                        cnt = 1

        return result