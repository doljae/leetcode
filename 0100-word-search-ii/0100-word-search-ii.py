from typing import List

class Node:
    def __init__(self):
        self.val = ""
        self.has_value = False
        self.next = {}

class Trie:
    def __init__(self):
        node = Node()
        node.val = "head"
        self.head = node

    def insert(self, word):
        cur = self.head
        for char in word:
            if char not in cur.next:
                node = Node()
                node.val = char
                cur.next[char] = node
            cur = cur.next[char]
        cur.has_value = True

    def search(self, word):
        cur = self.head
        for char in word:
            if char not in cur.next:
                return None
            cur = cur.next[char]
        return cur

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        height, width = len(board), len(board[0])
        result = set()
        trie = Trie()
        visited = [[False] * width for _ in range(height)]

        for word in words:
            trie.insert(word)

        def dfs(x, y, node, path):
            if not (0 <= x < height) or not (0 <= y < width) or visited[x][y]:
                return

            char = board[x][y]
            if char not in node.next:
                return

            node = node.next[char]
            path.append(char)

            if node.has_value:
                result.add("".join(path))

            visited[x][y] = True
            dfs(x + 1, y, node, path)
            dfs(x - 1, y, node, path)
            dfs(x, y + 1, node, path)
            dfs(x, y - 1, node, path)
            visited[x][y] = False

            path.pop()

        for i in range(height):
            for j in range(width):
                dfs(i, j, trie.head, [])

        return list(result)