class Solution:
    def __init__(self):
        self.result = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.result = max(self.result, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.result