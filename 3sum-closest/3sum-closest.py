class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = 0
        answer_gap = float("inf")
        for i in range(0, len(nums) - 2):
            start, end = i + 1, len(nums) - 1

            while start < end:
                cur = nums[i] + nums[start] + nums[end]
                if abs(cur - target) < answer_gap:
                    answer_gap = abs(cur - target)
                    answer = cur

                if cur < target:
                    start += 1
                elif cur > target:
                    end -= 1
                elif cur == target:
                    return cur

        return answer