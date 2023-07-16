import collections


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(list(s))
        most_common_char, most_common_char_count = counter.most_common(1)[0]
        target_length = len(s) // 2 if len(s) % 2 == 0 else len(s) // 2 + 1
        if most_common_char_count > target_length:
            return ""

        board = [""] * len(s)
        board_index = 0

        while counter[most_common_char] > 0:
            board[board_index] = most_common_char
            board_index += 2
            counter[most_common_char] -= 1

        for char, count in counter.most_common():
            while count > 0:
                if board_index >= len(s):
                    board_index = 1
                board[board_index] = char
                count -= 1
                board_index += 2

        return "".join(board)