class Solution:
    answer = 1

    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(cur, length):
            if not cur.left and not cur.right:
                self.answer = min(self.answer, length) if self.answer != 1 else length
                return

            if cur.left:
                dfs(cur.left, length + 1)
            if cur.right:
                dfs(cur.right, length + 1)

        if not root:
            return 0

        dfs(root, 1)

        return self.answer