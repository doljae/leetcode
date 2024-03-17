from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        if not root:
            return "*"

        visited = []
        q = deque([root])

        while q:
            cur = q.popleft()
            if cur is None:
                visited.append("*")
                continue
            else:
                visited.append(str(cur.val))

            q.append(cur.left if cur.left else None)
            q.append(cur.right if cur.right else None)

        return ".".join(visited)

    def deserialize(self, data):
        if data == "*":
            return None

        nodes = list(map(lambda x: int(x) if x != "*" else x, data.split(".")))

        root = temp = TreeNode(nodes[0])
        visited = deque([])
        q = deque(nodes[1:])

        while q:
            left = q.popleft()
            if left == "*":
                left_node = None
            else:
                left_node = TreeNode(left)

            temp.left = left_node
            visited.append(left_node)

            right = q.popleft()
            if right == "*":
                right_node = None
            else:
                right_node = TreeNode(right)

            temp.right = right_node
            visited.append(right_node)

            while visited and visited[0] is None:
                visited.popleft()

            if not visited:
                break

            temp = visited.popleft()

        return root
