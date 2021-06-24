class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque([])
        q.append((root, 0))
        dict1 = defaultdict(list)
        dict1[0].append(root)
        while q:
            cur_node, cur_level = q.popleft()
            if cur_node.left:
                dict1[cur_level + 1].append(cur_node.left)
                q.append((cur_node.left, cur_level + 1))
            if cur_node.right:
                dict1[cur_level + 1].append(cur_node.right)
                q.append((cur_node.right, cur_level + 1))
        # for level in dict1:
        #     for i in range(len(dict1[level]) - 1):
        #         dict1[level][i].next = dict1[level][i + 1]
        for level in dict1:
            # print(dict1[level])
            for i in range(len(dict1[level]) - 1):
                dict1[level][i].next = dict1[level][i + 1]
        return root