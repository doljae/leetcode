class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list1 = list(pattern)
        list2 = s.split()

        dict1 = {}
        set1 = set()

        if len(list1) != len(list2):
            return False

        for i in range(len(list1)):
            t1, t2 = list1[i], list2[i]

            if t1 not in dict1:
                if t2 in set1:
                    return False
                set1.add(t2)
                dict1[t1] = t2

            if dict1[t1] != t2:
                return False

        return True
