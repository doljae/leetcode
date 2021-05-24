class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        '''
        A ~ Z, 1 ~ 26
        AA ~ AZ 27 ~ 52
        '''
        answer = 0
        list1 = list(columnTitle)[::-1]
        for i in range(len(list1)):
            target = list1[i]
            answer += ((ord(target) - 64) * pow(26, i))
        return answer