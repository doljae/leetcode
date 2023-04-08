class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        index1 = 0
        while index1 < len(nums) - 3:
            a = nums[index1]
            index2 = index1 + 1
            while index2 < len(nums) - 2:
                b = nums[index2]
                index3, index4 = index2 + 1, len(nums) - 1
                while index3 < index4:
                    c, d = nums[index3], nums[index4]
                    temp = a + b + c + d
                    if temp == target:
                        result.append([a, b, c, d])
                        while index3 < len(nums) - 1 and nums[index3 + 1] == c:
                            index3 += 1
                        while index4 > index2 and nums[index4 - 1] == d:
                            index4 -= 1
                        index3, index4 = index3 + 1, index4 - 1
                    elif temp > target:
                        index4 -= 1
                    elif temp < target:
                        index3 += 1
                while index2 < len(nums) - 2 and nums[index2 + 1] == b:
                    index2 += 1
                index2 += 1
            while index1 < len(nums) - 3 and nums[index1 + 1] == a:
                index1 += 1
            index1 += 1

        return result