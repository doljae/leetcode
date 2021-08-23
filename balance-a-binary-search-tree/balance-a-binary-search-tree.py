class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        seq = []

        def in_order(cur):
            if cur.left:
                in_order(cur.left)
            seq.append(cur.val)
            if cur.right:
                in_order(cur.right)

        in_order(root)

        def make_bst(candidate):
            mid = len(candidate) // 2
            cur_root = TreeNode(candidate[mid])
            if candidate[:mid]:
                cur_root.left = make_bst(candidate[:mid])
            if candidate[mid + 1:]:
                cur_root.right = make_bst(candidate[mid + 1:])

            return cur_root

        return make_bst(seq)