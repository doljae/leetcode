from typing import *


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if not stack or token not in ["+", "-", "/", "*"]:
                stack.append(int(token))

            else:
                b, a = stack.pop(), stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "/":
                    stack.append(trunc(a / b))
                elif token == "*":
                    stack.append(a * b)
            # print(stack)

        return stack[-1]