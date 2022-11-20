class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        result = 0
        nums = deque(nums)
        nums2 = []
        while nums:
            target = nums.popleft()
            if not nums2:
                nums2.append(target)
            elif nums2[-1] != target:
                nums2.append(target)
        
        print(nums2)
        for i in range(len(nums2)):
            if i == 0 or i == len(nums2) - 1:
                continue
            elif nums2[i-1] < nums2[i] > nums2[i+1]:
                result += 1
            elif nums2[i-1] > nums2[i] < nums2[i+1]:
                result += 1
            
        return result
            
        