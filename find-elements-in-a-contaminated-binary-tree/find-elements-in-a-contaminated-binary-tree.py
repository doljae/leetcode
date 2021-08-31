# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.visited = {0}
        self.recover(self.root)

    def find(self, target: int) -> bool:
        if target in self.visited:
            return True
        return False

    def recover(self, cur):
        if cur.left:
            cur.left.val = cur.val * 2 + 1
            self.visited.add(cur.left.val)
            self.recover(cur.left)
        if cur.right:
            cur.right.val = cur.val * 2 + 2
            self.visited.add(cur.right.val)
            self.recover(cur.right)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)