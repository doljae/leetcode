# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        board = defaultdict(int)
        
        q = deque([])
        q.append((root, 1))
        
        while q:
            cur_node, cur_level = q.popleft()
            board[cur_level] += cur_node.val
            
            if cur_node.left:
                q.append((cur_node.left, cur_level+1))
            
            if cur_node.right:
                q.append((cur_node.right, cur_level+1))
        
        return Counter(board).most_common()[0][0]
            
            