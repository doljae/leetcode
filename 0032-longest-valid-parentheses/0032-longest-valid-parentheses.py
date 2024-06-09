class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = []

        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            else:
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(index)

        result = 0
        if not stack:
            return len(s)

        a, b = len(s), 0
        while stack:
            b = stack.pop()
            result = max(result, a - b - 1)
            a = b

        result = max(result, a)

        return result