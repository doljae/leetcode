# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        stack = []
        temp = []
        cur = root
        while True:
            while cur:
                temp.append(cur)
                stack.append(cur)
                cur = cur.left
            if not stack:
                break
            cur = stack.pop()
            cur = cur.right
        for item in temp:
            print(item.val)
        print()
        for i in range(1, len(temp)):
            temp[i-1].left = None
            temp[i-1].right = temp[i]
        # for item in temp:
        #     print(item.right.val)
        # print()
        return temp[0] if temp else []
