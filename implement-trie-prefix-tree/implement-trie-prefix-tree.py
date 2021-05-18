class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        cur = self.head
        for char in word:
            if char not in cur.child:
                new_node = Node(char)
                cur.child[char] = new_node
            cur = cur.child[char]
        cur.child["*"] = "!"

    def search(self, word: str) -> bool:
        cur = self.head
        for char in word:
            if char not in cur.child:
                return False
            cur = cur.child[char]
        if "*" in cur.child:
            return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for char in prefix:
            if char not in cur.child:
                return False
            cur = cur.child[char]
        return True


class Node:
    def __init__(self, val="0"):
        self.val = val
        self.child = {}

    def __str__(self):
        return f"val: {self.val}, child:{self.child}"