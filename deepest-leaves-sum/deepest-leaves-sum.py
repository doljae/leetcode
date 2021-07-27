class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = deque([(root, 0)])
        visited = [(root, 0)]
        while q:
            cur_node, cur_level = q.popleft()
            next_level = cur_level + 1
            if cur_node.left:
                visited.append((cur_node.left, next_level))
                q.append((cur_node.left, next_level))
            if cur_node.right:
                visited.append((cur_node.right, next_level))
                q.append((cur_node.right, next_level))

        max_level = visited[-1][1]
        answer = visited[-1][0].val
        visited.pop()
        while visited and visited[-1][1] == max_level:
            answer += visited[-1][0].val
            visited.pop()
        return answer