class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        stack=nums[::-1]
        k = k%len(nums)
        
        left,right=len(nums)-k, k 
        
        stack=stack[:right][::-1]+stack[right:][::-1]
        
        for i in range(len(stack)):
            nums[i]=stack[i]
        
        print(nums)
        