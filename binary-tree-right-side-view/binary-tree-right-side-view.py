# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        answer, trace = [], defaultdict(int)
        q = deque([(root, 0)])
        while q:
            cur_node, cur_level = q.popleft()
            trace[cur_level] = cur_node.val
            if cur_node.left:
                q.append((cur_node.left, cur_level + 1))
            if cur_node.right:
                q.append((cur_node.right, cur_level + 1))
        for level in trace:
            answer.append(trace[level])
        return answer