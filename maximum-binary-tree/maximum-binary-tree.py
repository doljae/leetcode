class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(cur_list):
            if not cur_list:
                return None
            pivot = cur_list.index(max(cur_list))

            cur_node = TreeNode(cur_list[pivot], None, None)
            left_list = cur_list[:pivot]
            right_list = cur_list[pivot + 1:]

            cur_node.left = dfs(left_list)
            cur_node.right = dfs(right_list)

            return cur_node

        return dfs(nums)
