class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_list = [i for i in range(len(nums))]
        new_nums = list(map(lambda x, y: (x, y), nums, index_list))
        new_nums.sort()
        start, end = 0, len(new_nums) - 1
        while start < end:
            temp = new_nums[start][0] + new_nums[end][0]
            if temp < target:
                start += 1
            elif temp == target:
                return [new_nums[start][1], new_nums[end][1]]
            elif temp > target:
                end -= 1