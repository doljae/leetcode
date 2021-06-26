import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pocket = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pocket:
            return False
        self.pocket.add(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pocket:
            return False
        self.pocket.remove(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(list(self.pocket))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
