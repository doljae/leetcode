class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        sums = [0] * 10001

        for num in nums:
            sums[num] += num

        for i in range(2, len(sums)):
            sums[i] = max(sums[i - 1], sums[i - 2] + sums[i])

        return sums[-1]