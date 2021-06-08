class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        for char in s:
            if char.isalnum():
                stack.append(char.lower())

        if len(stack) % 2 == 1:
            return stack[:len(stack) // 2] == stack[len(stack) // 2 + 1:][::-1]
        else:
            return stack[:len(stack) // 2] == stack[len(stack) // 2:][::-1]
