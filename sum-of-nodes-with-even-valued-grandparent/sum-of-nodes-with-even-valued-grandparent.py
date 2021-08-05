class Solution:
    answer = 0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(cur_node, cur_parent, cur_grandpa):
            if cur_grandpa:
                target = cur_grandpa.val
                if target % 2 == 0:
                    self.answer += cur_node.val

            new_parent, new_grandpa = cur_node, cur_parent
            if cur_node.left:
                dfs(cur_node.left, new_parent, new_grandpa)

            if cur_node.right:
                dfs(cur_node.right, new_parent, new_grandpa)

        dfs(root, 0, None)
        return self.answer
