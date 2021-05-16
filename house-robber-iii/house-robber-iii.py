class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(cur):
            if not cur:
                return [0, 0]
            left = dfs(cur.left)
            right = dfs(cur.right)

            return [max(left) + max(right), left[0] + right[0] + cur.val]

        answer = dfs(root)
        return max(answer)