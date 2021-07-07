class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left, right = None, None
        if not nums:
            return []
        if len(nums)%2 == 0:
            left, right = nums[:len(nums)//2],nums[len(nums)//2:]
        else:
            left,right=nums[:len(nums)//2+1],nums[len(nums)//2+1:]
        answer=[]
        p1,p2=0,0
        while True:
            if p1<len(left):
                answer.append(left[p1])
                p1+=1
            if p2<len(right):
                answer.append(right[p2])
                p2+=1
            if p1 == len(left) and p2== len(left):
                break
        return answer
                