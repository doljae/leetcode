class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        root1_seq = deque([])
        root2_seq = deque([])
        answer = []

        def in_order(cur, flag):
            if cur.left:
                in_order(cur.left, flag)
            if flag == 1:
                root1_seq.append(cur.val)
            else:
                root2_seq.append(cur.val)
            if cur.right:
                in_order(cur.right, flag)
        if root1:
            in_order(root1, 1)
        if root2:
            in_order(root2, 2)

        while root1_seq or root2_seq:
            if not root1_seq:
                answer += list(root2_seq)
                break
            elif not root2_seq:
                answer += list(root1_seq)
                break

            head1, head2 = root1_seq[0], root2_seq[0]
            if head1 >= head2:
                answer.append(root2_seq.popleft())
            else:
                answer.append(root1_seq.popleft())

        return answer