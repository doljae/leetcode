from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.max_frequency = 0
        self.board = defaultdict(list)
        self.counter = defaultdict(int)

    def push(self, val: int) -> None:
        self.counter[val] += 1
        self.board[self.counter[val]].append(val)
        self.max_frequency = max(self.max_frequency, self.counter[val])

    def pop(self) -> int:
        result = self.board[self.max_frequency].pop()
        self.counter[result] -= 1

        if not self.board[self.max_frequency]:
            self.max_frequency -= 1

        return result