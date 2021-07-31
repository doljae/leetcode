class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def bstToGst(self, root):
        def dfs(cur, val, saved):
            if not cur.left and not cur.right:
                cur.val += saved
                return cur.val

            right = 0
            if cur.right:
                right = dfs(cur.right, val, saved)
            cur.val += right

            if not right:
                cur.val += saved

            saved = cur.val if not saved else max(saved, cur.val)

            left = 0
            if cur.left:
                left = dfs(cur.left, cur.val, saved)

            return left if left else cur.val

        dfs(root, 0, 0)
        return root