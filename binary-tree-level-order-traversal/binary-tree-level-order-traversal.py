class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        answer = []
        if not root:
            return []
        q = deque([])
        q.append((root, 0))
        trace = {}
        while q:
            cur_node, cur_level = q.popleft()
            if cur_level not in trace:
                trace[cur_level] = [cur_node.val]
            else:
                trace[cur_level].append(cur_node.val)
            if cur_node.left:
                q.append((cur_node.left, cur_level + 1))
            if cur_node.right:
                q.append((cur_node.right, cur_level + 1))
        for level in trace:
            answer.append(trace[level])
        return answer