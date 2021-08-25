class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) <= k:
            self.stack = list(map(lambda x: x + val, self.stack))
        else:
            self.stack = list(map(lambda x: x + val, self.stack[:k])) + self.stack[k:]