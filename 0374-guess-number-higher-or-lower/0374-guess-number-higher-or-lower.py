# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left, right = 1, n
        
        while True:
            # print(left, right)
            mid = (left + right) // 2
            temp = guess(mid)
            
            if temp == 0:
                return mid
            elif temp > 0:
                left = mid + 1
            elif temp < 0:
                right = mid - 1
        
        return -1