class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        answer = []
        left, right = 0, 0
        for char in s:
            if char == "(":
                left += 1
            else:
                right += 1
            stack.append(char)
            if left == right:
                if stack:
                    stack.pop()
                answer += stack[1:]
                stack.clear()
                left, right = 0, 0

        return "".join(answer)