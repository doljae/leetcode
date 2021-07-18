class Solution:
    def numberOfSteps(self, num: int) -> int:
        cur = num
        answer = 0
        while cur != 0:
            if cur % 2 == 0:
                cur /= 2
            else:
                cur -= 1
            answer += 1
        return answer