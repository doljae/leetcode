# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return []

            left, right = [], []
            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)

            return left + [root.val] + right

        visited = sorted(dfs(root))
        answer = float("inf")
        for i in range(len(visited) - 1):
            answer = min(answer, abs(visited[i + 1] - visited[i]))

        return answer