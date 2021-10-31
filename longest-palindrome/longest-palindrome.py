class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        
        answer = 0
        max_mid_len = 0
        for key in counter:
            length = counter[key]
            if length % 2 == 0 :
                answer += length
            else:
                answer += length // 2 * 2
                if answer % 2 == 0 and length % 2 == 1 :
                    answer += 1
        
        return answer