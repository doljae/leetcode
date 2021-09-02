class Solution:
    def countVowelStrings(self, n: int) -> int:
        a, e, i, o, u = [1], [1], [1], [1], [1]

        for index in range(2, n + 1):
            a.append(a[-1] + e[-1] + i[-1] + o[-1] + u[-1])
            e.append(e[-1] + i[-1] + o[-1] + u[-1])
            i.append(i[-1] + o[-1] + u[-1])
            o.append(o[-1] + u[-1])
            u.append(u[-1])

        return a[-1] + e[-1] + i[-1] + o[-1] + u[-1]