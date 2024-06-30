from collections import deque
class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        lis=[]
        dq=deque()
        if n==1:
            return [arr[0]]
        if k==1:
            return arr
            
        for i in range(k):
            while dq and arr[i]>=arr[dq[-1]]:
                dq.pop()
            dq.append(i)    
        for i in range(k,n):    
            lis.append(arr[dq[0]])
            while dq and dq[0]<=i-k:
                dq.popleft()
            while dq and arr[i]>=arr[dq[-1]]:
                dq.pop()
            dq.append(i)
        lis.append(arr[dq[0]])    
        return lis    