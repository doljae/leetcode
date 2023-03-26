import random


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.list.append(val)
        self.dict[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False

        val_index, last_val = self.dict[val], self.list[-1]
        self.list[val_index], self.dict[last_val] = last_val, val_index
        self.list.pop()
        self.dict.pop(val)
        return True

    def getRandom(self) -> int:
        return self.list[random.randint(0, len(self.list) - 1)]
