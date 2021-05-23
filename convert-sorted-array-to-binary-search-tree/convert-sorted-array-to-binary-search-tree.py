# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dfs(cur_list):
            if not cur_list:
                return None
            mid = len(cur_list) // 2
            cur_node = TreeNode(cur_list[mid])
            cur_node.right = dfs(cur_list[mid + 1:])
            cur_node.left = dfs(cur_list[:mid])
            return cur_node

        return dfs(nums)