class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # edge case: [0,0,0]
        count1, count2, candi1, candi2 = 0, 0, 0, 1

        for num in nums:
            if num == candi1:
                count1 += 1
            elif num == candi2:
                count2 += 1
            elif count1 == 0:
                candi1, count1 = num, 1
            elif count2 == 0:
                candi2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        return [num for num in [candi1, candi2] if nums.count(num) > len(nums) / 3]