from typing import *


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for target in range(1, n + 1):
            temp = str(target)
            if target % 3 == 0 and target % 5 == 0:
                temp = "FizzBuzz"
            elif target % 3 == 0:
                temp = "Fizz"
            elif target % 5 == 0:
                temp = "Buzz"
            answer.append(temp)
        return answer