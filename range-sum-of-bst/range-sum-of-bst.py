class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(cur):
            if not cur:
                return 0
            answer = 0
            if low < cur.val:
                answer += dfs(cur.left)

            if cur.val < high:
                answer += dfs(cur.right)

            if low <= cur.val <= high:
                answer += cur.val

            return answer

        return dfs(root)