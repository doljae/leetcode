from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict1 = Counter(s)
        answer = len(s)
        
        for char in t:
            if char in dict1 and dict1[char] > 0:
                dict1[char]-=1
                answer -= 1

        return answer