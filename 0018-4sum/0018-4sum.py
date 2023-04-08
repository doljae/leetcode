class Solution:  # 1084 ms, faster than 37.26%
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(l, r, k, target, path, out):  # [l, r] inclusive
            if k == 2:
                while l < r:
                    if nums[l] + nums[r] == target:
                        out.append(path + [nums[l], nums[r]])
                        while l+1 < r and nums[l] == nums[l+1]: l += 1  # Skip duplicate nums[l]
                        l, r = l + 1, r - 1
                    elif nums[l] + nums[r] > target:
                        r -= 1  # Decrease sum
                    else:
                        l += 1  # Increase sum
                return

            while l < r:
                dfs(l+1, r, k - 1, target - nums[l], path + [nums[l]], out)
                while l+1 < r and nums[l] == nums[l+1]: l += 1  # Skip duplicate nums[i]
                l += 1

        def kSum(k):  # k >= 2
            ans = []
            nums.sort()
            dfs(0, len(nums)-1, k, target, [], ans)
            return ans

        return kSum(4)