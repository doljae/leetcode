class Solution:
    answer = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(cur):
            if low <= cur.val <= high:
                self.answer += cur.val

            if not cur.left and not cur.right:
                return

            if cur.left:
                dfs(cur.left)

            if cur.right:
                dfs(cur.right)

        dfs(root)
        return self.answer