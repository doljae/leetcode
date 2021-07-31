class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def dfs(cur):
            if not cur.left and not cur.right:
                return True if cur.val == 1 else False

            left, right = None, None
            if cur.left:
                left = dfs(cur.left)
            if cur.right:
                right = dfs(cur.right)

            if left is False or left is None:
                cur.left = None
            if right is False or right is None:
                cur.right = None

            return True if left is True or right is True or cur.val == 1 else False

        dfs(root)
        return root if root.val == 1 or root.left or root.right else None
