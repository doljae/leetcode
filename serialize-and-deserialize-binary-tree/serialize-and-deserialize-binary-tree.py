class Codec:

    def serialize(self, root):
        if not root:
            return ""

        answer = [str(root.val)]
        q = deque([root])

        while q:
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
                answer.append(str(cur.left.val))
            else:
                answer.append("#")
            if cur.right:
                q.append(cur.right)
                answer.append(str(cur.right.val))
            else:
                answer.append("#")

        # print(answer)
        return "_".join(answer)

    def deserialize(self, data):
        if not data:
            return None

        nodes = data.split("_")
        root = TreeNode(int(nodes[0]))
        q2 = deque([root])
        q1 = deque(nodes[1:])
        while q2:
            cur = q2.popleft()

            left, right = q1.popleft(), q1.popleft()

            if left != "#":
                left_node = TreeNode(int(left))
                cur.left = left_node
                q2.append(left_node)

            if right != "#":
                right_node = TreeNode(int(right))
                cur.right = right_node
                q2.append(right_node)

        return root