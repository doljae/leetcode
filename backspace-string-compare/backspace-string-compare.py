class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []
        p1, p2 = 0, 0
        e1, e2 = len(s), len(t)

        while p1 < e1 or p2 < e2:

            if p1 < e1:
                c1 = s[p1]
                if stack1 and c1 == "#":
                    stack1.pop()
                elif c1 != "#":
                    stack1.append(c1)

            if p2 < e2:
                c2 = t[p2]
                if stack2 and c2 == "#":
                    stack2.pop()
                elif c2 != "#":
                    stack2.append(c2)

            p1, p2 = p1 + 1, p2 + 1


        return "".join(stack1) == "".join(stack2)
