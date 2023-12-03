class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {}
        for index, char in enumerate(s):
            last_index[char] = index

        stack, visited = [], set()

        for index, char in enumerate(s):
            if char not in visited:
                while stack and stack[-1] > char and last_index[stack[-1]] > index:
                    visited.remove(stack.pop())
                stack.append(char)
                visited.add(char)

        return "".join(stack)