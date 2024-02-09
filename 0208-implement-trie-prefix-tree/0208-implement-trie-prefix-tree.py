class Trie:

    def __init__(self):
        self.root = Node("HEAD")

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                new_node = Node(char)
                cur.children[char] = new_node
            cur = cur.children[char]

        cur.check = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]

        return cur.check

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]

        return cur.check or len(cur.children) > 0


class Node:
    def __init__(self, val):
        self.val = val
        self.check = False
        self.children = {}

    def __str__(self):
        return f"Node(val={self.val}), check={self.check}, children={self.children.keys()}"
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)