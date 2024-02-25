class Solution:
    def isValidBST(self,
                   root: Optional[TreeNode]) -> bool:

        if not root:
            return False

        stack = []

        def dfs(node):
            if node.left:
                dfs(node.left)
            stack.append(node.val)
            if node.right:
                dfs(node.right)
        
        dfs(root)

        return stack == sorted(stack) and len(stack) == len(set(stack))