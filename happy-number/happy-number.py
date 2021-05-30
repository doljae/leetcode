from functools import reduce


class Solution:
    def isHappy(self, n: int) -> bool:
        def phase_one(num):
            return list(map(int, list(str(num))))

        def phase_two(input_list):
            return reduce(lambda acc, cur: acc + cur * cur, input_list, 0)

        cur = n
        set1 = set()
        set1.add(cur)
        while cur != 1:
            temp = phase_two(phase_one(cur))
            if temp in set1:
                return False
            set1.add(cur)
            cur = temp
        return True if cur == 1 else False