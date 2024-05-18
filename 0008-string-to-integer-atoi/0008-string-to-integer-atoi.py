class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()

        if not s:
            return 0

        board = []
        flag = False
        is_positive = True

        for char in s:
            if not board:
                if char == "+":
                    if flag:
                        return 0
                    is_positive = True
                    flag = True
                elif char == "-":
                    if flag:
                        return 0
                    is_positive = False
                    flag = True
                elif char.isdecimal():
                    board.append(char)
                else:
                    return 0
            else:
                if char.isdecimal():
                    board.append(char)
                else:
                    result = int("".join(board)) if is_positive else -int("".join(board))
                    if result <= -pow(2, 31):
                        return -pow(2, 31)
                    elif result >= pow(2, 31) - 1:
                        return pow(2, 31) - 1
                    else:
                        return result
        
        if not board:
            return 0
        
        result = int("".join(board)) if is_positive else -int("".join(board))
        if result <= -pow(2, 31):
            return -pow(2, 31)
        elif result >= pow(2, 31) - 1:
            return pow(2, 31) - 1
        else:
            return result