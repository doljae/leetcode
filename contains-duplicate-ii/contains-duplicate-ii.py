class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dict1={}
        for index, num in enumerate(nums):
            if num not in dict1:
                dict1[num] = [index]
            else:
                dict1[num].append(index)
        
        for key in dict1:
            temp = dict1[key]
            
            while len(temp)>1:
                cur=temp.pop()
                if abs(temp[-1] - cur) <= k:
                    return True
        
        return False