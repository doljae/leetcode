class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        cur = root
        prev = None
        while True:
            if cur is None:
                if val < prev.val:
                    prev.left = TreeNode(val)
                else:
                    prev.right = TreeNode(val)
                break

            prev = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        return root