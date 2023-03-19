from collections import Counter, defaultdict


class FreqStack:

    def __init__(self):
        self.frequency = Counter()
        self.map = defaultdict(list)
        self.max_frequency = 0

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        self.max_frequency = max(self.max_frequency, self.frequency[val])
        self.map[self.frequency[val]].append(val)

    def pop(self) -> int:
        target = self.map[self.max_frequency].pop()
        if not self.map[self.max_frequency]:
            self.max_frequency -= 1

        self.frequency[target] -= 1

        return target
