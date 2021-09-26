class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1:
            return True

        max_target = 2
        while (max_target + 1) * (max_target + 1) <= num:
            max_target += 1

        cur = num
        temp = 2
        answer = []
        while cur != 1:
            temp2 = 0
            while cur % temp == 0:
                temp2 += 1
                cur = cur // temp

            answer.append(temp2)
            temp += 1
            if temp > max_target:
                break

        if cur != 1:
            answer.append(1)

        for item in answer:
            if item % 2 != 0:
                return False

        return True