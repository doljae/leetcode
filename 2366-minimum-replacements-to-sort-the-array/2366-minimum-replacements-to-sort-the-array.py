class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0
        prev = nums[n - 1]
        for ind in range(n - 2, -1, -1):
            num = nums[ind]
            k = ceil(num / prev)

            # (k - 1) is the minimum number of times you'll have to split
            ret += k - 1
            # (num // k) is the maximal number you can create from splitting (k - 1) times
            prev = num // k

        return ret