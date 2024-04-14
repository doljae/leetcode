from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        board = []

        char_list = deque(list(s))

        while char_list:
            char = char_list.popleft()
            if char.isdigit():
                temp = [char]
                while char_list and char_list[0].isdigit():
                    temp.append(char_list.popleft())

                int_char = int("".join(temp))
                if board and board[-1] == "-":
                    board.pop()
                    board.append(-int_char)
                else:
                    board.append(int_char)
            elif char == "+":
                continue
            elif char == "-":
                board.append(char)
            elif char == " ":
                continue
            elif char == "(":
                board.append(char)
            elif char == ")":
                temp = 0
                while board and board[-1] != "(":
                    temp += board.pop()
                board.pop()
                if board and board[-1] == "-":
                    board.pop()
                    board.append(-temp)
                else:
                    board.append(temp)

        # print(board)
        return sum(board)