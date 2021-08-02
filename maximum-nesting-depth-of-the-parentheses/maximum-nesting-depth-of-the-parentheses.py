class Solution:
    def maxDepth(self, s: str) -> int:
        answer = 0
        stack =[]
        for char in s:
            if char=="(":
                stack.append(char)
            elif char==")":
                answer = max(answer, len(stack))
                stack.pop()
        return answer