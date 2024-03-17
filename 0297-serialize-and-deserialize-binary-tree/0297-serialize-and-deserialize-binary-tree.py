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
            return ""

        result = [root.val]
        q = deque([root])

        while q:
            cur = q.popleft()

            if cur.left:
                q.append(cur.left)
                result.append(cur.left.val)
            else:
                result.append("*")

            if cur.right:
                q.append(cur.right)
                result.append(cur.right.val)
            else:
                result.append("*")

        while result and result[-1] == "*":
            result.pop()

        return ".".join(list(map(str, result)))

    def deserialize(self, data):
        if not data:
            return None

        nodes = []
        for val in data.split("."):
            if val != "*":
                nodes.append(int(val))
            else:
                nodes.append(None)

        root = TreeNode(nodes[0])

        q = deque(nodes[1:])
        temp_index = 0
        result = [root]
        while q:
            temp = result[temp_index]
            left = q.popleft()
            left_node = TreeNode(left)
            temp.left = left_node if left else None
            result.append(left_node)
            if q:
                right = q.popleft()
                right_node = TreeNode(right)
                temp.right = right_node if right else None
                result.append(right_node)

            temp_index += 1
            if result[temp_index].val is None:
                temp_index += 1

        return root