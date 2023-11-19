class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_count, b_count = 0, 0
        stack = []
        before_two = None
        for color in colors:
            if not stack:
                stack.append(color)
            elif len(stack) == 1:
                before_two = stack[-1]
                stack.append(color)
            else:
                if stack[-1] == before_two == color:
                    if color == "A":
                        a_count += 1
                    else:
                        b_count += 1
                else:
                    before_two = stack[-1]
                    stack.append(color)

        if a_count == 0:
            return False
        return True if a_count > b_count else False
